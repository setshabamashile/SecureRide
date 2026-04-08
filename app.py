from flask import Flask
from flask_cors import CORS
from routes.sessions import sessions

app = Flask(__name__)

# Enable CORS (VERY IMPORTANT)
CORS(app)

# Register blueprint
app.register_blueprint(sessions)

# Test route (optional)
@app.route('/')
def home():
    return {"message": "SecureRide API running"}

if __name__ == '__main__':
    app.run(debug=True)
