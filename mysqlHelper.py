import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# MySQL Connection
def dbInitConnection(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), database=os.getenv('DB_NAME')):
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = db.cursor()
    return db, cursor

# Close MySQL Connection
def dbCloseConnection(db, cursor):
    cursor.close()
    db.close()