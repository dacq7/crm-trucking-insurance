from app.extensions import db
from datetime import datetime

class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(120), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    dl_years_experience = db.Column(db.Integer, nullable=False)

    license_number = db.Column(db.String(80))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
