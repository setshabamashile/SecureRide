from flask import Blueprint, request, jsonify
from db import get_connection
from datetime import datetime

sessions = Blueprint('sessions', __name__)

# GET all sessions
@sessions.route('/sessions', methods=['GET'])
def get_sessions():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM UserSession")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

# CREATE session (login)
@sessions.route('/sessions', methods=['POST'])
def add_session():
    data = request.json

    login_time = datetime.now()  # ✅ correct timestamp

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO UserSession (session_id, user_id, login_time, status) VALUES (%s,%s,%s,%s)",
        (
            data['session_id'],
            data['user_id'],
            login_time,
            data['status']
        )
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Session created"}), 201

# UPDATE session (logout)
@sessions.route('/sessions/<int:session_id>', methods=['PUT'])
def update_session(session_id):
    data = request.json

    logout_time = datetime.now()  # ✅ correct timestamp

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE UserSession SET logout_time=%s, status=%s WHERE session_id=%s",
        (
            logout_time,
            data['status'],
            session_id
        )
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Session updated (logged out)"})

# DELETE session
@sessions.route('/sessions/<int:session_id>', methods=['DELETE'])
def delete_session(session_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM UserSession WHERE session_id=%s", (session_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Session deleted"})
