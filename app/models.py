from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Property {self.id}>'
    
db.create_all()