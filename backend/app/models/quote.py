from app.extensions import db
from datetime import datetime

class Quote(db.Model):
    __tablename__ = "quotes"

    id = db.Column(db.Integer, primary_key=True)

    price = db.Column(db.Float, nullable=False)
    insurer = db.Column(db.String(120))
    mga = db.Column(db.String(120))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign Key
    policy_id = db.Column(db.Integer, db.ForeignKey("policies.id"), nullable=False)
