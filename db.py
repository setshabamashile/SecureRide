 
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",  # IP of the database machine
        user="root",
        password="Admin123.",
        database="LeapfrogApp"
    )