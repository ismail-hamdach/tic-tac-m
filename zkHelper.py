from zk import ZK, const
import os
from dotenv import load_dotenv

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
        # Real-time attendance monitoring
        for att in conn.live_capture():
            if att is None:
                pass
            else:
                print(f"Real-time attendance: User ID: {att.user_id}, Time: {att.timestamp}, Status: {att.punch}")

                # Check if the attendance log is already stored
                cursor.execute(
                    "SELECT * FROM attendance_logs WHERE user_id = %s AND timestamp = %s AND status = %s", 
                    (att.user_id, att.timestamp, att.punch)
                )
                result = cursor.fetchone()

                # If the log does not exist, insert it into the database
                if result is None:
                    sql = "INSERT INTO attendance_logs (user_id, timestamp, status) VALUES (%s, %s, %s)"
                    val = (att.user_id, att.timestamp, att.punch)
                    cursor.execute(sql, val)
                    db.commit()
                    print(f"New attendance stored: User ID = {att.user_id}, Timestamp = {att.timestamp}, Status = {att.punch}")
                else:
                    print(f"Duplicate attendance detected. Skipping: User ID = {att.user_id}, Timestamp = {att.timestamp}, Status = {att.punch}")

    except Exception as e:
        print(f"Error monitoring real-time attendance: {e}")

    finally:
        # Close the database connection if necessary
        cursor.close()
        db.close()