from zk import ZK, const
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
ip = os.getenv('DEVICE_IP')
port = int(os.getenv('DEVICE_PORT'))


def zkInitConnection():
    return ZK(ip, port)

def connect_device(zk):
    try:
        conn = zk.connect()
        print("Connected to device")
        return conn
    except Exception as e:
        print(f"Error connecting to device: {e}")
        return None

def fetch_users(conn):
    try:
        conn.disable_device()
        users = conn.get_users()
        for user in users:
            privilege = 'User' if user.privilege != const.USER_ADMIN else 'Admin'
            print(f"User ID: {user.user_id}, Name: {user.name}, Privilege: {privilege}")
        conn.enable_device()
    except Exception as e:
        print(f"Error fetching users: {e}")


def fetch_attendance(conn):
    try:
        attendances = conn.get_attendance()
        for att in attendances:
            print(f"User ID: {att.user_id}, Time: {att.timestamp}, Status: {att.punch}")
    except Exception as e:
        print(f"Error fetching attendance: {e}")


def monitor_real_time(conn, db, cursor):
    try:
        for att in conn.live_capture():
            if att is None:
                continue

            print(f"Real-time attendance: User ID: {att.user_id}, Time: {att.timestamp}, Status: {att.punch}")

            check_flag = 0
            if att.punch == 0:  # Check-in
                cursor.execute(
                    "SELECT * FROM attendance_logs WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1",
                    (att.user_id,)
                )
                last_record = cursor.fetchone()

                if last_record and last_record[5] is None:  # check_out is the 5th column
                    cursor.execute(
                        "UPDATE attendance_logs SET check_out = %s WHERE id = %s",
                        (att.timestamp, last_record[0])  # Assuming id is the 1st column
                    )
                    check_flag = 1
                else:
                    cursor.execute(
                        "INSERT INTO attendance_logs (user_id, check_in) VALUES (%s, %s)",
                        (att.user_id, att.timestamp)
                    )
                    check_flag = 2

            elif att.punch == 1:  # Check-out
                cursor.execute(
                    "SELECT * FROM attendance_logs WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1",
                    (att.user_id,)
                )
                last_record = cursor.fetchone()

                if last_record and last_record[5] is None:  # check_out is the 6th column
                    cursor.execute(
                        "UPDATE attendance_logs SET check_out = %s WHERE id = %s",
                        (att.timestamp, last_record[0])  # id is the 1st column
                    )
                    check_flag = 1

            # New logic for attendance_checks
            today = datetime.now().date()
            cursor.execute(
                "SELECT * FROM attendance_checks WHERE date = %s",
                (today,)
            )
            today_record = cursor.fetchone()

            if not today_record:
                cursor.execute(
                    "INSERT INTO attendance_checks (date, check_in, check_out, updated_at) VALUES (%s, 0, 0, %s)",
                    (today, datetime.now())
                )
                cursor.execute("SELECT LAST_INSERT_ID()")
                last_id = cursor.fetchone()[0]
                today_record = (last_id, today, 0, 0, datetime.now())

            if check_flag == 1:
                cursor.execute(
                    "UPDATE attendance_checks SET check_out = check_out + 1, updated_at = %s WHERE id = %s",
                    (datetime.now(), today_record[0])  # Assuming id is the 1st column
                )
            elif check_flag == 2:
                cursor.execute(
                    "UPDATE attendance_checks SET check_in = check_in + 1, updated_at = %s WHERE id = %s",
                    (datetime.now(), today_record[0])  # Assuming id is the 1st column
                )

            db.commit()
            print(f"Attendance processed: User ID = {att.user_id}, Timestamp = {att.timestamp}, Status = {'Check-in' if att.punch == 0 else 'Check-out'}")

    except Exception as e:
        print(f"Error monitoring real-time attendance: {e}")

    finally:
        cursor.close()
        db.close()