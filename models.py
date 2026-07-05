from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    fullname = db.Column(db.String(100), nullable=False)

    dob = db.Column(db.Date, nullable=False)

    email = db.Column(db.String(120), nullable=False)

    glucose = db.Column(db.Float, nullable=False)

    haemoglobin = db.Column(db.Float, nullable=False)

    cholesterol = db.Column(db.Float, nullable=False)

    condition = db.Column(db.String(150))

    risk_level = db.Column(db.String(20))

    recommendation = db.Column(db.String(250))