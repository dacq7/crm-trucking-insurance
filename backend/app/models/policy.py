from app.extensions import db
from datetime import datetime

class Policy(db.Model):
    __tablename__ = "policies"

    id = db.Column(db.Integer, primary_key=True)

    policy_type = db.Column(db.String(100), nullable=False)
    insurer = db.Column(db.String(120), nullable=False)
    mga = db.Column(db.String(120), nullable=False)

    limits = db.Column(db.String(120))

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    status = db.Column(db.String(50), default="active")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
