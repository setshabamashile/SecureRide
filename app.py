 
from flask import Flask
from routes.trips import trips
from routes.users import users
from routes.vehicle import vehicle
from routes.verification import verification
from routes.emergency_contact import emergency_contacts
from routes.alert import alerts
from routes.report import reports
from routes.user_session import sessions
# import other routes...

app = Flask(__name__)

app.register_blueprint(trips)
app.register_blueprint(users)
app.register_blueprint(vehicle)
app.register_blueprint(verification)
app.register_blueprint(emergency_contacts)
app.register_blueprint(alerts)
app.register_blueprint(reports)
app.register_blueprint(sessions, url_prefix='/api')
# register others...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
