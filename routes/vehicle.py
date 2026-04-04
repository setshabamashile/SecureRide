

from flask import Blueprint, request, jsonify
from db import get_connection

vehicle = Blueprint('vehicle', __name__)

@vehicle.route('/vehicle', methods=['GET'])
def get_vehicles():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Vehicle")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@vehicle.route('/vehicle/add', methods=['POST'])
def add_vehicle():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Vehicle (vehicle_id, model, registration_number, driver_id) VALUES (%s,%s,%s,%s)",
        (data['vehicle_id'], data['model'], data['registration_number'], data['driver_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Vehicle added"})

@vehicle.route('/vehicle/update', methods=['POST'])
def update_vehicle():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Vehicle SET model=%s, registration_number=%s, driver_id=%s WHERE vehicle_id=%s",
        (data['model'], data['registration_number'], data['driver_id'], data['vehicle_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Vehicle updated"})

@vehicle.route('/vehicle/delete', methods=['POST'])
def delete_vehicle():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Vehicle WHERE vehicle_id=%s", (data['vehicle_id'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Vehicle deleted"})