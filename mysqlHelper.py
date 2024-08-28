import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# MySQL Connection
def dbInitConnection(host=os.getenv('PYTHON_DB_HOST'), port=os.getenv('PYTHON_DB_PORT'), user=os.getenv('PYTHON_DB_USER'), password=os.getenv('PYTHON_DB_PASSWORD'), database=os.getenv('PYTHON_DB_NAME')):
    print(host,
        port,
        user,
        password,
        database)
    db = mysql.connector.connect(
        host=host,
        port=port,
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