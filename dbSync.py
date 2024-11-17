import mysql.connector
from zk import ZK, const
from zkHelper import zkInitConnection
from helpers import stptime
from mysqlHelper import dbInitConnection, dbCloseConnection
import os
from dotenv import load_dotenv

load_dotenv()

PYTHON_DB_host = os.getenv('PYTHON_DB_HOST')
PYTHON_DB_user = os.getenv('PYTHON_DB_USER')
PYTHON_DB_password = os.getenv('PYTHON_DB_PASSWORD')
PYTHON_DB_name = os.getenv('PYTHON_DB_NAME')

device_ip = os.getenv('DEVICE_IP')
device_port = os.getenv('DEVICE_PORT')

def dbSync():
    try:
        # MySQL Connection
        db, cursor = dbInitConnection(PYTHON_DB_host, PYTHON_DB_user, PYTHON_DB_password, PYTHON_DB_name)
        print("Connected to MySQL database")

        # ZKTeco Device Connection
        zk = zkInitConnection()
        conn = zk.connect()
        print("Connected to device")

        logs = conn.get_attendance()
        print(f"Fetched {len(logs)} logs from device")

        # Check for older logs not stored
        cursor.execute("SELECT MAX(timestamp) FROM attendance_logs")
        last_stored_timestamp = cursor.fetchone()[0] or '1970-01-01 00:00:00'
        print(f"Last stored timestamp: {last_stored_timestamp}")

        # TODO: Check for logs not stored in MySQL using other method because this method ignore logs stored in period of lost connection
        # Filter logs not stored
        logs_to_store = [log for log in logs if stptime(log.timestamp) > stptime(last_stored_timestamp)]
        print(f"Storing {len(logs_to_store)} logs")

        # Store logs in MySQL and delete from device
        for log in logs_to_store:
            sql = "INSERT INTO attendance_logs (user_id, timestamp, status) VALUES (%s, %s, %s)"
            val = (int(log.user_id), stptime(log.timestamp), log.punch)
            cursor.execute(sql, val)
            db.commit()
            print(f"Log user_id: {log.user_id} timestamp: {stptime(log.timestamp)} status: {log.punch} stored in MySQL database")   

        print("Logs synced")

        # Clear logs from the device
        conn.clear_attendance()
        print("Logs cleared from device")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        dbCloseConnection(db, cursor)
        print("Disconnected from MySQL database")
        conn.disconnect()
        print("Disconnected from device")

dbSync()

