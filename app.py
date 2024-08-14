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
zk = zkInitConnection(os.getenv('DEVICE_IP'), os.getenv('DEVICE_PORT'), timeout=5, password=0)



def main():
    conn = connect_device(zk)
    if conn:
        db, cursor = dbInitConnection(os.getenv('DB_HOST'), os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_NAME'))
        dbSync()
        # fetch_attendance(conn)
        monitor_real_time(conn, db, cursor)
        conn.disconnect()
        print("Disconnected from device")

if __name__ == "__main__":
    main()
