@users.route('/emergency_contacts', methods=['GET'])
def get_emergency_contacts():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM EmergencyContact")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@users.route('/emergency_contacts/add', methods=['POST'])
def add_emergency_contact():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO EmergencyContact (contact_id, user_id, name, phone) VALUES (%s,%s,%s,%s)",
        (data['contact_id'], data['user_id'], data['name'], data['phone'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Emergency contact added"})

@users.route('/emergency_contacts/update', methods=['POST'])
def update_emergency_contact():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE EmergencyContact SET user_id=%s, name=%s, phone=%s WHERE contact_id=%s",
        (data['user_id'], data['name'], data['phone'], data['contact_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Emergency contact updated"})

@users.route('/emergency_contacts/delete', methods=['POST'])
def delete_emergency_contact():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM EmergencyContact WHERE contact_id=%s", (data['contact_id'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Emergency contact deleted"})
