from server.admin import Admin
from flask import jsonify, make_response, request, session

def login():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        
        email = data.get('email')
        fetched_password = data.get('password')
        
        if not email or not fetched_password:
            return jsonify({'error': 'Email or password cannot be empty'})

        admin = Admin.query.filter_by(email=email).first()
        if admin:
            password = admin.password
            if password and password != fetched_password:
                return jsonify({'error': 'Invalid credentials'})

            # Set a cookie to store the email of the logged-in user
            response = make_response(jsonify({'islogged': 'loggedin'}))
            response.set_cookie('email', email)
            return response

        return jsonify({'error': 'Admin not found'}), 404

def logout():
    # Clear the email cookie to log the user out
    response = make_response(jsonify({'message': 'Logged out'}))
    response.set_cookie('email', '', expires=0)
    return response
