from zk import ZK, const
from datetime import datetime
import json
from zkHelper import zkInitConnection, connect_device, fetch_users, fetch_attendance, monitor_real_time
# from dbSync import dbSync
from mysqlHelper import dbInitConnection, dbCloseConnection
import os
from dotenv import load_dotenv

load_dotenv()
db_host = os.getenv('PYTHON_DB_HOST')
db_user = os.getenv('PYTHON_DB_USER')
db_password = os.getenv('PYTHON_DB_PASSWORD')
db_name = os.getenv('PYTHON_DB_NAME')
db_port = os.getenv('PYTHON_DB_PORT')

# Connection details



def main():
    try:
        zk = zkInitConnection()
        conn = connect_device(zk)
        if conn:
            print("Connected to device")
            db, cursor = dbInitConnection(db_host, db_port, db_user, db_password, db_name)
            # dbSync()
            # fetch_attendance(conn)
            monitor_real_time(conn, db, cursor)
            dbCloseConnection(db, cursor)
            conn.disconnect()
            print("Disconnected from device")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
