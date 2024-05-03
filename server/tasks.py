from server.databaseconf import db

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'))  # Foreign key to the Tickets table
    ticket = db.relationship('Tickets', back_populates='tasks')
    