 

from flask import Blueprint, request, jsonify
from db import get_connection

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@users.route('/users/add', methods=['POST'])
def add_user():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Users (user_id, name, surname, email, password, role, phone) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (data['user_id'], data['name'], data['surname'], data['email'], data['password'], data['role'], data['phone'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "User added"})

@users.route('/users/update', methods=['POST'])
def update_user():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Users SET name=%s, surname=%s, email=%s, role=%s, phone=%s WHERE user_id=%s",
        (data['name'], data['surname'], data['email'], data['role'], data['phone'], data['user_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated"})

@users.route('/users/delete', methods=['POST'])
def delete_user():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Users WHERE user_id=%s", (data['user_id'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted"})