from flask import Blueprint, request, jsonify
import MySQLdb.cursors
from db import get_connection

alerts = Blueprint('alerts', __name__)

@alerts.route('/alerts', methods=['GET'])
def get_alerts():
    conn = get_connection()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)  # fixed
    cursor.execute("SELECT * FROM Alert")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@alerts.route('/alerts/add', methods=['POST'])
def add_alert():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Alert (alert_id, trip_id, alert_type, alert_message, created_at) VALUES (%s,%s,%s,%s,%s)",
        (data['alert_id'], data['trip_id'], data['alert_type'], data['alert_message'], data.get('created_at'))
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Alert added"})

@alerts.route('/alerts/update', methods=['POST'])
def update_alert():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Alert SET alert_type=%s, alert_message=%s WHERE alert_id=%s",
        (data['alert_type'], data['alert_message'], data['alert_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Alert updated"})

@alerts.route('/alerts/delete', methods=['POST'])
def delete_alert():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Alert WHERE alert_id=%s", (data['alert_id'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Alert deleted"})
