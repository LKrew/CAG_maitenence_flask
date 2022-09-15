from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

partLog_events = db.Table('partLog_events',
db.Column('partLog_id', db.String(34), db.ForeignKey('partLog.logId')),
db.Column('event_id', db.String(34), db.ForeignKey('event.eventID'))
)