# db.py
import MySQLdb
from flask import current_app

def get_connection():
    return MySQLdb.connect(
        host='172.20.10.4',      # Your MySQL device IP address
        user='root',               # Your MySQL username
        password='system123',           # Your MySQL password
        database='LeapfrogApp',     # Your database name
        port=3306
    )
