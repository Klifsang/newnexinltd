from server.models import Client
from flask import jsonify, request
from server.databaseconf import db

def clients():
    if request.method == 'GET':
        clients = Client.query.all()
        client_list = []
        for client in clients:
            client_list.append({
                'id': client.id,
                'name': client.name,
                'email': client.email,
                'phone_number': client.phone_number,
                'address': client.address
            })
        return jsonify(client_list)
    elif request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        address = data.get('address')
        client = Client(name = name,email=email,phone_number=phone_number, address=address)
        db.session.add(client)
        db.session.commit()
        inserted_client = {
            'id': client.id,
            'name': client.name,
            'email': client.email,
            'phone_number': client.phone_number,
            'address': client.address
        }
        return jsonify(inserted_client)
    elif request.method == 'DELETE':
        client_id = request.args.get('id')
        client = Client.query.get(client_id)
        if client:
            db.session.delete(client)
            db.session.commit()
            return f"Client with ID {client_id} deleted"
        else:
            return f"Client with ID {client_id} not found", 404