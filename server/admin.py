from server.databaseconf import db
from sqlalchemy.orm import validates

class Admin(db.Model):
    __tablename__ = 'admin'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50))  
    phone_number = db.Column(db.String(15))  # Specify length if required.
    address = db.Column(db.String)
    availability = db.Column(db.String)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    @validates('first_name', 'last_name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name is required")
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        return name
    
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if phone_number and not all(c.isdigit() or c in '- ()+' for c in phone_number):
            raise ValueError("Phone number must contain only digits and standard separators (dashes, spaces, plus).")
        if len(phone_number) > 15:
            raise ValueError("Phone number must be less than 15 characters")
        return phone_number
    
    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Invalid email format")
        return email
    
    def __repr__(self):
        return f"<Admin {self.first_name} {self.last_name}>"