from flask import Blueprint, request, jsonify
from db import get_connection

sessions = Blueprint('sessions', __name__)

# GET all sessions
@sessions.route('/api/sessions', methods=['GET'])
def get_sessions():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM UserSession")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

# ADD session
@sessions.route('/api/sessions/add', methods=['POST'])
def add_session():
    data = request.get_json()

    user_id = data.get('user_id')
    status = data.get('status')

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO UserSession (user_id, status) VALUES (%s, %s)"
    cursor.execute(query, (user_id, status))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Session added successfully"})
