from app import db


class Pizza(db.Model):
    __tablename__ = 'pizza'
    identifier = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
