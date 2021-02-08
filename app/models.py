from datetime import datetime
from app import db


class DeviceTest(db.Model):
    __tablename__ = 'device_tests'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now)
    device_type = db.Column(db.String(33))
    operator = db.Column(db.String(33))
    time = db.Column(db.DateTime)
    success = db.Column(db.Integer)
