import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="4787",
        database="notificaciones_db"
    )
    return conn
