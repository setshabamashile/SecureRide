from db import get_connection

# Test the connection
conn = get_connection()

if conn:
    print("Successfully connected to MySQL Workbench database!")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM UserSession")
    results = cursor.fetchall()
    
    print(f"\n Found {len(results)} sessions:")
    for row in results:
        print(row)
    
    cursor.close()
    conn.close()
else:
    print("Failed to connect to database")
