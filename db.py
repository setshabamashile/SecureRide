import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="3306",
        password="22@Sizwe",
        database="secureride"
    )
return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
