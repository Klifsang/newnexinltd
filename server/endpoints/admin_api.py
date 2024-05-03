from server.models import Admin
from flask import jsonify, request
from server.databaseconf import db

def admin():
    if request.method == 'GET':
        
        admin = Admin.query.all()
        admin_list = []
        for admin in admin:
            admin_list.append({
                'id': admin.id,
                'first_name': admin.first_name,
                'last_name': admin.last_name,
                'user_name': admin.user_name,
                'password': admin.password,
                'phone_number': admin.phone_number,
                'address': admin.address,
                'availability': admin.availability,
                'email': admin.email
            })
        return jsonify(admin_list)
    
    elif request.method == 'POST':
        data = request.get_json()
        print(jsonify(data))
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        user_name = data.get('email')
        password = data.get('password')
        phone_number = data.get('contactNumber')
        address = data.get('address')
        email = data.get('email')
        
        admin = Admin(first_name=first_name, last_name=last_name, user_name=user_name, password=password, phone_number=phone_number, address=address, availability='available', email=email)
        
        
        db.session.add(admin)
        db.session.commit()
        return jsonify({
            'id': admin.id,
            'first_name': admin.first_name,
            'last_name': admin.last_name,
            'user_name': admin.user_name,
            'password': admin.password,
            'phone_number': admin.phone_number,
            'address': admin.address,
            'availability': admin.availability,
            'email': admin.email
        }), 201
        # return jsonify(inserted_admin), 201
    
    elif request.method == 'DELETE':
        admin_id = request.args.get('id')
        admin = Admin.query.get(admin_id)
        if admin:
            db.session.delete(admin)
            db.session.commit()
            return f"Client with ID {admin_id} deleted"
        else:
            return f"Client with ID {admin_id} not found", 404
        
    elif request.method == 'PATCH':
        admin_id = request.args.get('id')
        admin = Admin.query.get(admin_id)
        if not admin:
            return jsonify({'message': 'Admin not found'}), 404
        data = request.get_json()
        if 'availability' in data:
            admin.availability = data['availability']
        db.session.commit()
        return jsonify({'message': 'Availability updated successfully'}), 200
    