from backend.models.db import db
import datetime


class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=True, nullable=False)
    data = db.Column(db.String(120), unique=True, nullable=False)
    created_by_id = person_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.name
