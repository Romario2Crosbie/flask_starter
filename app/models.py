from . import db

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    property_type = db.Column(db.String(20), nullable=False, default='apartment')
    num_bedrooms = db.Column(db.Integer, nullable=False)
    num_bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200), nullable=False)
    
    
    def __init__ (self, title, property_type, num_bedrooms, num_bathrooms, location, price, description, photo):
        self.title = title
        self.property_type = property_type
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.location = location
        self.price = price
        self.description =description
        self.photo = photo
        

    def __repr__(self):
        return f'<properties {self.id}>'


        