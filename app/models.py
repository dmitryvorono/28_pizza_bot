from app import db


pizza_sizes = db.Table('pizza_sizes',
    db.Column('pizza_size_id', db.Integer, db.ForeignKey('pizza_size.id'), primary_key=True),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'), primary_key=True)
)


class Pizza(db.Model):
    __tablename__ = 'pizza'
    identifier = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    weight = db.Column(db.Integer)
    size = db.relationship('PizzaSize', secondary=pizza_sizes)
    price = db.Column(db.Float)


class PizzaSize(db.Model):
    __tablename__ = 'pizza_size'
    identifier = db.Column('id', db.Integer, primary_key=True)
    size = db.Column(db.Integer)
    