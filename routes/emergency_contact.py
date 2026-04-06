from flask import Blueprint, request, jsonify
from db import get_connection

emergency_contacts = Blueprint('emergency_contacts', __name__)

# GET all emergency contacts
@emergency_contacts.route('/emergency_contacts', methods=['GET'])
def get_emergency_contacts():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM EmergencyContact")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

# CREATE emergency contact
@emergency_contacts.route('/emergency_contacts', methods=['POST'])
def add_emergency_contact():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO EmergencyContact (contact_id, user_id, name, phone) VALUES (%s,%s,%s,%s)",
        (
            data['contact_id'],
            data['user_id'],
            data['name'],
            data['phone']
        )
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Emergency contact created"}), 201

# UPDATE emergency contact
@emergency_contacts.route('/emergency_contacts/<int:contact_id>', methods=['PUT'])
def update_emergency_contact(contact_id):
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE EmergencyContact SET user_id=%s, name=%s, phone=%s WHERE contact_id=%s",
        (
            data['user_id'],
            data['name'],
            data['phone'],
            contact_id
        )
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Emergency contact updated"})

# DELETE emergency contact
@emergency_contacts.route('/emergency_contacts/<int:contact_id>', methods=['DELETE'])
def delete_emergency_contact(contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM EmergencyContact WHERE contact_id=%s", (contact_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Emergency contact deleted"})
