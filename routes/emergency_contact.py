from flask import Blueprint, request, jsonify
import MySQLdb.cursors
from db import get_connection

emergency_contact = Blueprint('emergency_contact', __name__)

@emergency_contact.route('/emergency_contact', methods=['GET'])
def get_emergency_contacts():
    conn = get_connection()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)  # fixed
    cursor.execute("SELECT * FROM EmergencyContact")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@emergency_contact.route('/emergency_contact/add', methods=['POST'])
def add_emergency_contact():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO EmergencyContact (contact_id, user_id, contact_name, contact_phone) VALUES (%s,%s,%s,%s)",
        (data['contact_id'], data['user_id'], data['contact_name'], data['contact_phone'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Emergency contact added"})

@emergency_contact.route('/emergency_contact/update', methods=['POST'])
def update_emergency_contact():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE EmergencyContact SET contact_name=%s, contact_phone=%s WHERE contact_id=%s",
        (data['contact_name'], data['contact_phone'], data['contact_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Emergency contact updated"})

@emergency_contact.route('/emergency_contact/delete', methods=['POST'])
def delete_emergency_contact():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM EmergencyContact WHERE contact_id=%s", (data['contact_id'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Emergency contact deleted"})
