from backend.models.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    entries_id = db.relationship('JournalEntry', backref='user', lazy=True)


    def __repr__(self):
        return '<User %r>' % self.username
