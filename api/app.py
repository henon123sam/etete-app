from flask import Flask
from supabase import create_client, Client

app = Flask(__name__)

# Supabase configuration
SUPABASE_URL = "https://jkiliqipfzfxqmsfcssp.supabase.co"
SUPABASE_KEY = "sb_publishable_Xz4YJx5VJB0rq1M8j4-QBw_L5ZZWHyp"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

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
    app.run(debug=True)