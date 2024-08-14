import mysql.connector
from zk import ZK, const
from helpers import stptime
from mysqlHelper import dbInitConnection, dbCloseConnection

def dbSync():
    try:
        # MySQL Connection
        db, cursor = dbInitConnection("localhost", "root", "", "tictacm")

        # ZKTeco Device Connection
        zk = ZK('192.168.2.250', port=4370, timeout=5, password=0)
        conn = zk.connect()
        logs = conn.get_attendance()

        # Check for older logs not stored
        cursor.execute("SELECT MAX(timestamp) FROM attendance_logs")
        last_stored_timestamp = cursor.fetchone()[0] or '1970-01-01 00:00:00'

        # Filter logs not stored
        logs_to_store = [log for log in logs if stptime(log.timestamp) > stptime(last_stored_timestamp)]

        # Store logs in MySQL and delete from device
        for log in logs_to_store:
            sql = "INSERT INTO attendance_logs (user_id, timestamp, status) VALUES (%s, %s, %s)"
            val = (log.user_id, stptime(log.timestamp), log.punch)
            cursor.execute(sql, val)
            db.commit()

        # Clear logs from the device
        conn.clear_attendance()
        print("Logs synced")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        dbCloseConnection(db, cursor)

