from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import datetime

db = SQLAlchemy()
ma = Marshmallow()
mi = Migrate()

class Form(db.Model):
    __tablename__ = "Form"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    form = db.Column(db.String, nullable=False, unique=True)
    date_create = db.Column(db.DateTime, default=datetime.datetime.now())
    
    def __init__(self, name, form):
        self.name = name
        self.form = form
    
class FormSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "form", "date_create")
    
form_schema = FormSchema()
forms_schema = FormSchema(many=True)
