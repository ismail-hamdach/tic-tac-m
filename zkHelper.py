from zk import ZK, const

def initConnection(ip, port=4370, timeout=5, password=0):
    return ZK(ip, port=port, timeout=timeout, password=password)

def connect_device():
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

def monitor_real_time(conn):
    try:
        for att in conn.live_capture():
            if att is None:
                print("No new attendance captured...")
            else:
                # serialize the attendance object to JSON
                # att_json = json.dumps(att)
                print(att)
                print(f"Real-time attendance: User ID: {att.user_id}, Time: {att.timestamp}, Status: {att.punch}")
    except Exception as e:
        print(f"Error monitoring real-time attendance: {e}")