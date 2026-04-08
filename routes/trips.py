
from flask import Blueprint, request, jsonify
import MySQLdb.cursors
from db import get_connection

trips = Blueprint('trips', __name__)

# List all trips
@trips.route('/trips', methods=['GET'])
def get_trips():
    conn = get_connection()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)  # fixed
    cursor.execute("SELECT * FROM Trip")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

# Insert a trip
@trips.route('/trips/add', methods=['POST'])
def add_trip():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Trip (trip_id, passenger_id, driver_id, pickup_location, destination, status) VALUES (%s,%s,%s,%s,%s,%s)",
        (data['trip_id'], data['passenger_id'], data['driver_id'], data['pickup_location'], data['destination'], data['status'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Trip added"})

# Update trip status
@trips.route('/trips/update', methods=['POST'])
def update_trip():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Trip SET status=%s WHERE trip_id=%s",
        (data['status'], data['trip_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Trip updated"})

# Delete a trip
@trips.route('/trips/delete', methods=['POST'])
def delete_trip():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Trip WHERE trip_id=%s", (data['trip_id'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Trip deleted"})
