from app.flask_server import db


class Pizza(db.Model):
    __tablename__ = 'pizzas'
    identifier = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    weight = db.Column(db.String)
