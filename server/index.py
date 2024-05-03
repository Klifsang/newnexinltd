from functools import wraps
# import os
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, redirect, request, send_from_directory, url_for
from flask_cors import CORS
from flask_migrate import Migrate
from server.databaseconf import db
from server.endpoints.client_api import clients
from server.endpoints.tickets_api import tickets
from server.endpoints.admin_api import admin
from server.endpoints.auth_api import login, logout


app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/dist',
    template_folder='../client/dist'
)
# Load environment variables from .env file
load_dotenv()
CORS(app, origins='*')  # Enable CORS with credentials support



app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///app.db" #DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


migrate = Migrate(app, db)

db.init_app(app)


@app.before_request
def before_request():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'message': 'Preflight request successful'})
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
        return response


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = request.cookies.get('username')
        if not username:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/protected')
@login_required
def protected():
    return jsonify({'message': 'This is a protected route'})
@app.route('/')
def index():
    return '<h3>Nexin LTD</h3>'

app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout, methods=['GET', 'POST'])
# app.add_url_rule('/check_login', 'check_login', check_login, methods=['GET', 'POST'])
app.add_url_rule('/admin', 'admin', admin, methods=['GET', 'POST', 'PATCH', 'DELETE'])
app.add_url_rule('/clients', 'clients', clients, methods=['GET', 'POST', 'PATCH', 'DELETE'])
app.add_url_rule('/tickets', 'tickets', tickets, methods=['GET', 'POST', 'DELETE', 'PATCH'])


if __name__ == '__main__':
    app.run(port=5555, debug=True)
