from flask import Flask
from routes.trips import trips
from routes.users import users
from routes.vehicle import vehicle
from routes.verification import verification
from routes.report import report
from routes.sessions import sessions
from routes.alert import alert
from routes.emergency_contact import emergency_contact



from flask_mysqldb import MySQL  # Add this import

app = Flask(__name__)

# === ADD DATABASE CONFIGURATION HERE ===
app.config['MYSQL_HOST'] = '172.20.10.4'      # Your MySQL device IP
app.config['MYSQL_USER'] = 'root'               # Your MySQL username
app.config['MYSQL_PASSWORD'] = 'system123'           # Your MySQL password
app.config['MYSQL_DB'] = 'LeapfrogApp'           # Your database name
app.config['MYSQL_PORT'] = 3306
# ======================================

# Initialize MySQL (add this after config)
mysql = MySQL(app)

# Make mysql available to blueprints (optional - depends on your blueprint code)
app.config['MYSQL'] = mysql

app.register_blueprint(trips)
app.register_blueprint(users)
app.register_blueprint(vehicle)
app.register_blueprint(verification)
app.register_blueprint(sessions)
app.register_blueprint(report)
app.register_blueprint(alert)
app.register_blueprint(emergency_contact)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
