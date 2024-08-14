from zk import ZK, const
from datetime import datetime
import json
from zkHelper import initConnection, fetch_users, fetch_attendance, monitor_real_time
# Connection details
zk = initConnection('192.168.2.250', port=4370, timeout=5, password=0)









def main():
    conn = connect_device()
    if conn:
        fetch_users(conn)
        fetch_attendance(conn)
        monitor_real_time(conn)
        conn.disconnect()
        print("Disconnected from device")

if __name__ == "__main__":
    main()
