@users.route('/reports', methods=['GET'])
def get_reports():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Report")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@users.route('/reports/add', methods=['POST'])
def add_report():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Report (report_id, trip_id, generated_by, report_details, created_at) VALUES (%s,%s,%s,%s,%s)",
        (data['report_id'], data['trip_id'], data['generated_by'], data['report_details'], data.get('created_at', 'CURRENT_TIMESTAMP'))
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Report added"})

@users.route('/reports/update', methods=['POST'])
def update_report():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Report SET trip_id=%s, generated_by=%s, report_details=%s WHERE report_id=%s",
        (data['trip_id'], data['generated_by'], data['report_details'], data['report_id'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Report updated"})

@users.route('/reports/delete', methods=['POST'])
def delete_report():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Report WHERE report_id=%s", (data['report_id'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Report deleted"})
