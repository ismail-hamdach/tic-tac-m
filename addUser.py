import mysql.connector
from zk import ZK, const
from mysqlHelper import dbInitConnection, dbCloseConnection
from zkHelper import zkInitConnection

# MySQL Database Connection 
db, cursor = dbInitConnection()

# Connect to the ZKTeco device
conn = None
zk = zkInitConnection('192.168.2.250', port=4370, timeout=5, password=0)

try:
    # Establish connection to the device
    conn = zk.connect()
    print("Connected to ZKTeco device")

    # Example user details
    user_id = "1235"  # This should be unique for each user
    user_name = "hamdach ismail"
    privilege = const.USER_DEFAULT  # Regular user
    password = "123456"  # Optional
    group_id = 0  # Optional
    user_card = None  # Optional
    user_fp_index = 0  # Index for the fingerprint (0 is typically the first finger)
    print(f"User {user_name} with ID {user_id} added to device")
    # Add the user to the device (without fingerprint yet)
    conn.set_user(uid=int(user_id), name=user_name, privilege=privilege, password=password, user_id=user_id)
    # conn.set_user(uid=1, name='John Doe', privilege=const.USER_DEFAULT, password='12345678', user_id='1')
    # print(f"User {user_name} with ID {user_id} added to device")

    # Enroll fingerprint for the user
    print("Please scan the fingerprint...")
    # conn.save_fp(user_id=user_id, user_fp_index=user_fp_index)
    conn.enroll_user(int(user_id))
    # template = conn.get_user_template(uid=int(user_id), temp_id=0) #temp_id is the finger to read 0~9
    # prin
    print(f"Fingerprint captured and enrolled for user {user_name}")

    # Store user information in MySQL database
    sql = "INSERT INTO users (user_id, user_name, privilege, password) VALUES (%s, %s, %s, %s)"
    val = (user_id, user_name, privilege, password)
    cursor.execute(sql, val)
    db.commit()
    print(f"User {user_name} with ID {user_id} stored in MySQL database")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close connections
    if conn:
        conn.disconnect()
    cursor.close()
    db.close()
