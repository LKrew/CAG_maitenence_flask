from db import db, partLog_events

class PartLogModel(db.Model):
    __tablename__  = 'partLogs'
    logId = db.Column(db.String(34), primary_key=True)
    serial = db.Column(db.String(80), db.ForeignKey('part.serial'))
    name = db.Column(db.String(80), db.ForeignKey('part.name'))
    position = db.Column(db.Integer, db.ForeignKey('part.position'))
    currentPostion = db.Column(db.Boolean(), )
    cagId = db.Column(db.String(80), db.ForeignKey('aircraft.cagId'))
    events = db.relationship('EventModel', secondary=partLog_events, backref='logs')

    