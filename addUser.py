import mysql.connector
from zk import ZK, const
from mysqlHelper import dbInitConnection, dbCloseConnection
from zkHelper import zkInitConnection
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

# MySQL Database Connection 
db, cursor = dbInitConnection()

# Connect to the ZKTeco device
conn = None
zk = zkInitConnection(os.getenv('DEVICE_IP'), os.getenv('DEVICE_PORT'), timeout=5, password=0)

def addUser(user_name):
    try:
        # Establish connection to the device
        conn = zk.connect()
        print("Connected to ZKTeco device")

        # Example user details
        user_id = str(uuid.uuid4())
        # user_name = "hamdach ismail"
        privilege = const.USER_DEFAULT  # Regular user
        password = "123456"  # Optional
        group_id = 0  # Optional
        user_card = None  # Optional
        user_fp_index = 0  # Index for the fingerprint (0 is typically the first finger)

        print(f"User {user_name} with ID {user_id} added to device")
        # Add the user to the device (without fingerprint yet)
        conn.set_user(uid=int(user_id), name=user_name, privilege=privilege, password=password, user_id=user_id)

        # Enroll fingerprint for the user
        print("Please scan the fingerprint...")
        conn.enroll_user(int(user_id))

        print(f"Fingerprint captured and enrolled for user {user_id}")

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
