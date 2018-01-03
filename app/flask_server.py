from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
admin = Admin(app, name='pizza bot', template_mode='bootstrap3')
from app import models, views
admin.add_view(ModelView(models.Pizza, db.session))
admin.add_view(ModelView(models.Choice, db.session))
