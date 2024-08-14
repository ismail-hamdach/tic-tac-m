import mysql.connector

# MySQL Connection
def dbInitConnection(host="localhost", user="root", password="", database="tictacm"):
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