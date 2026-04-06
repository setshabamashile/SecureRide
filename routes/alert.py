from flask import Blueprint, request, jsonify
from db import get_connection

alerts = Blueprint('alerts', __name__)

@users.route('/alerts', methods=['GET'])
def get_alerts():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Alert")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@users.route('/alerts/add', methods=['POST'])
def add_alert():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Alert (alert_id, trip_id, alert_type, location, alert_time) VALUES (%s,%s,%s,%s,%s)",
        (data['alert_id'], data['trip_id'], data['alert_type'], data['location'], data.get('alert_time', 'CURRENT_TIMESTAMP'))
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Alert added"})

@users.route('/alerts/update', methods=['POST'])
def update_alert():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Alert SET trip_id=%s, alert_type=%s, location=%s WHERE alert_id=%s",
        (data['trip_id'], data['alert_type'], data['location'], data['alert_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Alert updated"})

@users.route('/alerts/delete', methods=['POST'])
def delete_alert():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Alert WHERE alert_id=%s", (data['alert_id'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Alert deleted"})
