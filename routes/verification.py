 from flask import Blueprint, request, jsonify
import MySQLdb.cursors
from db import get_connection

verification = Blueprint('verification', __name__)

@verification.route('/verification', methods=['GET'])
def get_verifications():
    conn = get_connection()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)  # fixed
    cursor.execute("SELECT * FROM Verification")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@verification.route('/verification/add', methods=['POST'])
def add_verification():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Verification (verification_id, user_id, id_document, face_match_status, approval_status) VALUES (%s,%s,%s,%s,%s)",
        (data['verification_id'], data['user_id'], data['id_document'], data['face_match_status'], data['approval_status'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Verification added"})

@verification.route('/verification/update', methods=['POST'])
def update_verification():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Verification SET face_match_status=%s, approval_status=%s WHERE verification_id=%s",
        (data['face_match_status'], data['approval_status'], data['verification_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Verification updated"})

@verification.route('/verification/delete', methods=['POST'])
def delete_verification():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Verification WHERE verification_id=%s", (data['verification_id'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Verification deleted"})
