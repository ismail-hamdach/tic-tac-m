import mysql.connector
from zk import ZK, const
from mysqlHelper import dbInitConnection, dbCloseConnection
from zkHelper import zkInitConnection
import uuid
import os
from dotenv import load_dotenv



def addUser(user_name, ip_address, port):
    try:

        # MySQL Database Connection 
        # db, cursor = dbInitConnection()
        # print("Connected to MySQL database")

        # Connect to the ZKTeco device
        conn = None
        zk = zkInitConnection(ip_address, port)
        # Establish connection to the device
        conn = zk.connect()
        print("Connected to ZKTeco device")

        # Example user details
        user_id = str(uuid.uuid4().int)[:4]
        privilege = const.USER_DEFAULT  # Regular user
        password = "123456"  # Optional
        group_id = 0  # Optional
        user_card = None  # Optional
        user_fp_index = 0  # Index for the fingerprint (0 is typically the first finger)

        # Add the user to the device (without fingerprint yet)
        conn.set_user(uid=int(user_id), name=user_name, privilege=privilege, password=password, user_id=user_id)
        print(f"User {user_name} with ID {user_id} added to device")

        # Enroll fingerprint for the user
        print("Please scan the fingerprint...")
        conn.enroll_user(int(user_id))

        print(f"Fingerprint captured and enrolled for user {user_id}")

        # Store user information in MySQL database
        # sql = "INSERT INTO users (user_id, user_name, privilege, password) VALUES (%s, %s, %s, %s)"
        # val = (user_id, user_name, privilege, password)

        # cursor.execute(sql, val)
        # db.commit()
        # print(f"User {user_name} with ID {user_id} stored in MySQL database")

    except Exception as e:
        print(f"An error occurred: {e}")
        # TODO: remove user from scanner in this section
        raise


    finally:
        # Close connections
        if conn:
            conn.disconnect()
            print("Disconnected from ZKTeco device")
        # cursor.close()
        # db.close()
        # print("Disconnected from MySQL database")

    return user_id, user_name, privilege, password

def deleteUser(user_id):
    try:
        # Connect to the ZKTeco device
        zk = zkInitConnection()
        conn = zk.connect()
        print("Connected to ZKTeco device for deletion")

        # Delete the user from the device
        conn.delete_user(uid=int(user_id))
        print(f"User with ID {user_id} deleted from device")

    except Exception as e:
        print(f"An error occurred while deleting user: {e}")

    finally:
        # Close connection
        if conn:
            conn.disconnect()
            print("Disconnected from ZKTeco device for deletion")

# Example usage
# deleteUser("user_id_to_delete")

# addUser("Aymane El cadi")