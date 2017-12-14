from app import db


pizza_choices = db.Table('pizza_choices',
    db.Column('choice_id', db.Integer, db.ForeignKey('choices.id'), primary_key=True),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizzas.id'), primary_key=True)
)


class Pizza(db.Model):
    __tablename__ = 'pizzas'
    identifier = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    choices = db.relationship('Choice', secondary=pizza_choices)



class Choice(db.Model):
    __tablename__ = 'choices'
    identifier = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Float)
    