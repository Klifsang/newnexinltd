from server.databaseconf import db
from datetime import datetime
from enum import Enum
from server.databaseconf import db

class Tickets(db.Model):
    _tablename_ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    priority = db.Column(db.String)
    deadline = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    assign_to = db.Column(db.Integer, db.ForeignKey('admin.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    comments = db.Column(db.String, nullable=False)
    tasks = db.relationship('Task', back_populates='ticket')
    client = db.relationship("Client", back_populates="tickets")
    # tickets = db.relationship("Tickets", back_populates="admin")
    @property
    def days_remaining(self):
        return (self.deadline - datetime.utcnow()).days

    @property
    def is_urgent(self):
        return self.days_remaining < 3