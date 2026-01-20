from app.extensions import db
from datetime import datetime

class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)

    vin = db.Column(db.String(80), nullable=False)
    year = db.Column(db.String(10))
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    vehicle_type = db.Column(db.String(50))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign Key
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
