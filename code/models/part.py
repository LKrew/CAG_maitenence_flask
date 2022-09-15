from db import db

__tablename__ = 'parts'
cagId = db.Column(db.String(80), db.ForeignKey('aircraft.cagId'))
serial = db.Column(db.String(80), primary_key=True)
name = db.Column(db.String(80), primary_key=True)
position = db.Column(db.Integer, primary_key=True)
events = db.Column(db.String(80), db.ForeignKey('partLog.logId'))
partLog = db.relationship('PartLogModel')