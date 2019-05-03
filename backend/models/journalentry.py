from backend.models.db import db
import datetime


class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=True, nullable=False)
    data = db.Column(db.String(120), unique=True, nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'),
                              nullable=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<JournalEntry %r>' % self.id
