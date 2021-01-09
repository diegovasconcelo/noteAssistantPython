import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="master_python",
        port=8889
    )
    cursor = database.cursor(buffered=True)

    return [database, cursor]