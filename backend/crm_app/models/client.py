from crm_app.extensions import db
from datetime import datetime

class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)

    legal_name = db.Column(db.String(150), nullable=False)
    dot_number = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(120))

    physical_address = db.Column(db.String(255))
    mailing_address = db.Column(db.String(255))

    status = db.Column(db.String(50), default="prospect")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign Keys
    agent_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Relationships
    drivers = db.relationship("Driver", backref="client", lazy=True)
    vehicles = db.relationship("Vehicle", backref="client", lazy=True)
    policies = db.relationship("Policy", backref="client", lazy=True)
