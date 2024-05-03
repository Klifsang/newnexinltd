from datetime import datetime
from models import Tickets
from flask import jsonify, request
from server.databaseconf import db

def tickets():
    if request.method == 'GET':
        tickets = Tickets.query.all()
        ticket_list = []
        for ticket in tickets:
            ticket_list.append({
                'id' : ticket.id,
                'status' : ticket.status,  # Convert Enum to its value
                'priority' : ticket.priority,  # Convert Enum to its value
                'deadline' : ticket.deadline,
                'assign_to' : ticket.assign_to,
                'client_id' : ticket.client_id,
                'comments' : ticket.comments
            })
        return jsonify(ticket_list)
    elif request.method == 'POST':
        data = request.get_json()
        status = 'Open'
        priority = 'urgent'
        deadline = data.get('deadline')
        assign_to = None
        client_id = '1'
        ticket = Tickets(status=status, priority=priority, deadline=datetime.utcnow(), assign_to=assign_to, client_id=client_id, comments='urgent')
        db.session.add(ticket)
        db.session.commit()
        inserted_ticket = {
            'id': ticket.id,  
            'status': ticket.status,  
            'priority': ticket.priority, 
            'deadline': ticket.deadline,
            'assign_to': ticket.assign_to,
            'client_id': ticket.client_id,
            'comments': ticket.comments
        }
        return jsonify(inserted_ticket)

    elif request.method == 'DELETE':
        ticket_id = request.args.get('id')
        ticket = Tickets.query.get(ticket_id)
        if not ticket:
            return jsonify({'message': 'Ticket not found'}), 404
        db.session.delete(ticket)
        db.session.commit()
        return jsonify({'message': 'Ticket deleted successfully'}), 200
    
    
    elif request.method == 'PATCH':
        ticket_id = request.args.get('id')
        ticket = Tickets.query.get(ticket_id)
        if not ticket:
            return jsonify({'message': 'Ticket not found'}), 404
        data = request.get_json()
        if 'assign_to' in data:
            ticket.assign_to = data['assign_to']
        if 'status' in data:
            ticket.status = data['status']
        db.session.commit()
        return jsonify({'message': 'Ticket updated successfully'}), 200
    