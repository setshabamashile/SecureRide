@users.route('/sessions', methods=['GET'])
def get_sessions():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM UserSession")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@users.route('/sessions/add', methods=['POST'])
def add_session():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO UserSession (session_id, user_id, login_time, logout_time, status) VALUES (%s,%s,%s,%s,%s)",
        (data['session_id'], data['user_id'], data.get('login_time', 'CURRENT_TIMESTAMP'), data.get('logout_time'), data['status'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Session added"})

@users.route('/sessions/update', methods=['POST'])
def update_session():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE UserSession SET user_id=%s, logout_time=%s, status=%s WHERE session_id=%s",
        (data['user_id'], data.get('logout_time'), data['status'], data['session_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Session updated"})

@users.route('/sessions/delete', methods=['POST'])
def delete_session():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM UserSession WHERE session_id=%s", (data['session_id'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Session deleted"})
