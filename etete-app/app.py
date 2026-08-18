from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure a local SQLite database file named 'etete.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///etete.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Test Route for Customer Interface
@app.route('/')
def home():
    return "Etete Customer Interface is live!"

# Test Route for Employee Interface
@app.route('/employee')
def employee_dashboard():
    return "Etete Employee / Kitchen Dashboard"

# Test Route for Driver Interface
@app.route('/driver')
def driver_dashboard():
    return "Etete Driver Portal"

if __name__ == '__main__':
    # Automatically create database tables if they don't exist yet
    with app.app_context():
        db.create_all()
    app.run(debug=True)