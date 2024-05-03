from server.databaseconf import db
from sqlalchemy.orm import validates

class Client(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String, nullable=False)
    tickets = db.relationship('Tickets', back_populates='client')
    
    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, 'Invalid email address'
        return email

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        # Assuming phone numbers should be at least 10 characters long
        assert len(phone_number) >= 10, 'Phone number must be at least 10 characters long'
        return phone_number
    
    def __repr__(self):
        return f"<Client(name='{self.name}', email='{self.email}', phone_number='{self.phone_number}')>"