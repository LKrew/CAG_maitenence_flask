from turtle import position
from db import db

class EventModel(db.Model):

    __tablename__ = 'event'
    evetnId = db.Column(db.String(34))
    cagId = db.Column(db.String(80), db.ForeignKey('aircraft.cagId'))
    serial = db.Column(db.String(80), db.ForeignKey('part.serial'))
    name = db.Column(db.String(80), db.ForeignKey('part.name'))
    position = db.Column(db.Integer, db.ForeignKey('part.position'))
    # "intervals" : [
    #     {
    #         "unit" : "",
    #         "value" : "",
    #         "bufferValue" : "",
    #         "lastEventDate" : ""
    #     }
    # ],
    maintenanceType = db.Column(db.String(80))
    maintenanceSubType = db.Column(db.String(80))
    estimatedDueDate = db.Column(db.DateTime)
    dueDate = db.Column(db.DateTime)
    unit = db.Column(db.String(80))
    eventDescription = db.Column(db.String(256))
    eventStatus = db.Column(db.String(80))
    eventPriority = db.Column(db.Integer)
    lastEventDate = db.Column(db.DateTime)

    
    aircraft = db.relationship('AircraftModel')
    part = db.relationship('PartModel')