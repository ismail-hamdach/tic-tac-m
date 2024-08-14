from zk import ZK, const
from datetime import datetime
import json
from zkHelper import zkInitConnection, connect_device, fetch_users, fetch_attendance, monitor_real_time
from dbSync import dbSync
from mysqlHelper import dbInitConnection, dbCloseConnection
import os
from dotenv import load_dotenv

load_dotenv()

# Connection details



def main():
    try:
        zk = zkInitConnection()
        conn = connect_device(zk)
        if conn:
            print("Connected to device")
            db, cursor = dbInitConnection(os.getenv('DB_HOST'), os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_NAME'))
            dbSync()
            # fetch_attendance(conn)
            monitor_real_time(conn, db, cursor)
            conn.disconnect()
            print("Disconnected from device")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
