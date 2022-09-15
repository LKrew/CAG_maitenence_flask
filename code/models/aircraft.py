from db import db

class AircraftModel(db.Model):

    __tablename__ = 'aircraft'
    cagId = db.Column(db.String(80), primary_key=True)
    supplierId = db.Column(db.String(80))
    aircraftMake = db.Column(db.String(256))
    aircraftModel = db.Column(db.String(256))

