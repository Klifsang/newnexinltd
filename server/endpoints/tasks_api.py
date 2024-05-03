from datetime import datetime
from flask import jsonify, request
from server.databaseconf import db
from server.tickets import PriorityLevel, TicketStatus, Tickets

def task():
    if request.method == 'GET':
        task = Tickets.query.all()
        task_list = []
        for task in task:
            task_list.append({
                'id' : task.id,
                'status' : task.status.value,  # Convert Enum to its value
                'priority' : task.priority.value,  # Convert Enum to its value
                'deadline' : task.deadline,
                'assign_to' : task.assign_to,
                'client_id' : task.client_id,
                'comments' : task.comments
            })
        return jsonify(task_list)
    elif request.method == 'POST':
        data = request.get_json()
        priority = data.get('priority')
        deadline = data.get('deadline')
        assign_to = 'None'
        client_id = '1'
        ticket1 = Tickets(status=TicketStatus.OPEN, priority=priority, deadline=deadline, assign_to=assign_to, client_id=client_id, comments='Very urgent')
        # task = Task(status=status, priority=priority, deadline=deadline, assign_to=assign_to, client_id=client_id)
        db.session.add(ticket1)
        db.session.commit()
        inserted_task = {
            'id': task.id,  
            'status': task.status.value,  
            'priority': task.priority.value, 
            'deadline': task.deadline,
            'assign_to': task.assign_to,
            'client_id': task.client_id,
            'comments': task.comments
        }
        return jsonify(inserted_task)
    elif request.method == 'DELETE':
        task_id = request.args.get('id')
        task = Tickets.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return f"Task with ID {task_id} deleted"
        else:
            return f"Task with ID {task_id} not found", 404
    
    elif request.method == 'PATCH':
        task_id = request.args.get('id')
        task = Tickets.query.get(task_id)
        if not task:
            return jsonify({'message': 'Task not found'}), 404
        data = request.get_json()
        for key, value in data.items():
            setattr(task, key, value)
        db.session.commit()
        return jsonify(task._dict_), 200
    