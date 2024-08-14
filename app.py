from zk import ZK, const
from datetime import datetime
import json
from zkHelper import zkInitConnection, connect_device, fetch_users, fetch_attendance, monitor_real_time
from dbSync import dbSync
from mysqlHelper import dbInitConnection, dbCloseConnection

# Connection details
zk = zkInitConnection('192.168.2.250', port=4370, timeout=5, password=0)



def main():
    conn = connect_device(zk)
    if conn:
        db, cursor = dbInitConnection("localhost", "root", "", "tictacm")
        dbSync()
        # fetch_attendance(conn)
        monitor_real_time(conn, db, cursor)
        conn.disconnect()
        print("Disconnected from device")

if __name__ == "__main__":
    main()
