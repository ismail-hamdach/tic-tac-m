from zk import ZK, const  # Importing ZK library for device communication
import os  # Importing os module for environment variable handling
from dotenv import load_dotenv  # Importing dotenv to load environment variables from a .env file
from datetime import datetime, timedelta  # Importing datetime for handling date and time
import traceback

# Load environment variables from .env file
load_dotenv()
ip = os.getenv('DEVICE_IP')  # Get the device IP from environment variables
port = int(os.getenv('DEVICE_PORT'))  # Get the device port and convert it to an integer

# Function to initialize connection to the ZK device
def zkInitConnection(ip_address=ip, portNumber=port):
    return ZK(ip_address, int(portNumber))  # Return a ZK object initialized with IP and port

# Function to connect to the ZK device
def connect_device(zk):
    try:
        conn = zk.connect()  # Attempt to connect to the device
        print("Connected to device")  # Print success message
        return conn  # Return the connection object
    except Exception as e:
        print(f"Error connecting to device: {e}")  # Print error message if connection fails
        return None  # Return None if connection fails

# Function to fetch users from the device
def fetch_users(conn):
    try:
        conn.disable_device()  # Disable the device to prevent interference during data fetching
        users = conn.get_users()  # Fetch users from the device
        for user in users:  # Iterate through each user
            privilege = 'User' if user.privilege != const.USER_ADMIN else 'Admin'  # Determine user privilege
            print(f"User ID: {user.user_id}, Name: {user.name}, Privilege: {privilege}")  # Print user details
        conn.enable_device()  # Re-enable the device after fetching users
    except Exception as e:
        print(f"Error fetching users: {e}")  # Print error message if fetching fails

# Function to fetch attendance records from the device
def fetch_attendance(conn):
    try:
        attendances = conn.get_attendance()  # Fetch attendance records from the device
        for att in attendances:  # Iterate through each attendance record
            print(f"User ID: {att.user_id}, Time: {att.timestamp}, Status: {att.punch}")  # Print attendance details
    except Exception as e:
        print(f"Error fetching attendance: {e}")  # Print error message if fetching fails

# Function to monitor real-time attendance
def monitor_real_time(conn, db, cursor):
    print("Starting monitor_real_time function")  # Flag 1
    try:
        for att in conn.live_capture():  # Capture live attendance data
            print("Captured attendance data")  # Flag 2
            if att is None:  # Skip if no attendance data is captured
                continue

            print(f"Real-time attendance: User ID: {att.user_id}, Time: {att.timestamp}, Status: {att.punch}")  # Print real-time attendance

            check_flag = 0  # Initialize check_flag to track check-in/check-out status
            # Check-in logic
            if att.punch == 0:  # Check-in detected
                print("Processing check-in")  # Flag 3
                cursor.execute(
                    "SELECT * FROM attendance_logs WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1",  # Query to get the last attendance record for the user
                    (att.user_id,)
                )
                last_record = cursor.fetchone()  # Fetch the last attendance record

                if last_record and last_record['check_out'] is None:  # Check if last record exists and check_out is None
                    # New condition to check if the last check-in was done less than 5 minutes ago
                    if (att.timestamp - last_record['check_in']).total_seconds() < 300:  # 300 seconds = 5 minutes
                        print("Ignoring check-out: last check-in was less than 5 minutes ago")  # Debugging message
                        return  # Ignore the check-out
                    print('Update check_out in attendance_logs')
                    cursor.execute(
                        "UPDATE attendance_logs SET check_out = %s WHERE id = %s",  # Update check_out time for the last record
                        (att.timestamp, last_record['id'])  # Assuming id is the 1st column
                    )
                    check_flag = 1  # Set check_flag to indicate check-out was updated
                else:
                    print('Insert new check_in in attendance_logs')
                    cursor.execute(
                        "INSERT INTO attendance_logs (user_id, check_in) VALUES (%s, %s)",  # Insert new check-in record
                        (att.user_id, att.timestamp)
                    )
                    check_flag = 2  # Set check_flag to indicate a new check-in was created

            # Check-out logic
            elif att.punch == 1:  # Check-out detected
                print("Processing check-out")  # Flag 4
                cursor.execute(
                    "SELECT * FROM attendance_logs WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1",  # Query to get the last attendance record for the user
                    (att.user_id,)
                )
                last_record = cursor.fetchone()  # Fetch the last attendance record

                if last_record and last_record['check_out'] is None:  # Check if last record exists and check_out is None
                    # New condition to check if the last check-in was done less than 5 minutes ago
                    if (att.timestamp - datetime.fromisoformat(last_record['check_in'])).total_seconds() < 300:  # 300 seconds = 5 minutes
                        print("Ignoring check-out: last check-in was less than 5 minutes ago")  # Debugging message
                        return  # Ignore the check-out
                    print('Update check_out in attendance_logs')
                    cursor.execute(
                        "UPDATE attendance_logs SET check_out = %s WHERE id = %s",  # Update check_out time for the last record
                        (att.timestamp, last_record['id'])  # Assuming id is the 1st column
                    )
                    check_flag = 1  # Set check_flag to indicate check-out was updated

            # New logic for attendance_checks
            print("Checking attendance for today")  # Flag 5
            today = datetime.combine(datetime.now().date(), datetime.min.time())  # Set to today's date after midnight
            cursor.execute(
                "SELECT * FROM attendance_checks WHERE date >= %s",  # Query to check if there are records for today
                (today,)
            )
            today_record = cursor.fetchone()  # Fetch today's attendance record
            print(f"Fetched today's record: {today_record}")  # Debugging flag

            if not today_record:  # If no record exists for today
                print("No record found for today, inserting new record")  # Debugging flag
                cursor.execute(
                    "INSERT INTO attendance_checks (date, check_in, check_out, updated_at) VALUES (%s, 0, 0, %s)",  # Insert new record for today
                    (today, datetime.now())
                )
                # cursor.execute("SELECT LAST_INSERT_ID()")  # Get the ID of the last inserted record
                last_id = cursor.lastrowid  # Fetch the last inserted ID
                today_record = (last_id, today, 0, 0, datetime.now())  # Create a tuple for today's record
                print(f"Inserted new record with ID: {last_id}")  # Debugging flag

            # Update attendance_checks based on check_flag
            if check_flag == 1:  # If check-out was updated
                print("Updating attendance_checks for check-out")  # Flag 6
                cursor.execute(
                    "UPDATE attendance_checks SET check_out = check_out + 1, updated_at = %s WHERE id = %s",  # Increment check_out count
                    (datetime.now(), today_record['id'])  # Assuming id is the 1st column
                )
                print(f"Updated check-out count for record ID: {today_record['id']}")  # Debugging flag
            elif check_flag == 2:  # If new check-in was created
                print("Updating attendance_checks for check-in")  # Flag 7
                cursor.execute(
                    "UPDATE attendance_checks SET check_in = check_in + 1, updated_at = %s WHERE id = %s",  # Increment check_in count
                    (datetime.now(), today_record['id'])  # Assuming id is the 1st column
                )
                print(f"Updated check-in count for record ID: {today_record['id']}")  # Debugging flag

            db.commit()  # Commit the database changes
            print(f"Attendance processed: User ID = {att.user_id}, Timestamp = {att.timestamp}, Status = {'Check-in' if att.punch == 0 else 'Check-out'}")  # Print processed attendance details

    except Exception as e:
        print(f"Error monitoring real-time attendance: {e}\n{traceback.format_exc()}")  # Print error message if monitoring fails

    finally:
        cursor.close()  # Close the cursor
        db.close()  # Close the database connection