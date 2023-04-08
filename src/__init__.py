from flask import Flask
from flask_cors import CORS

from .Routes import api_form
from .Models import db, ma, mi, Form


app = Flask(__name__)
CORS(app)

#create base
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///form.db"

db.init_app(app)
ma.init_app(app)
mi.init_app(app, db)



#config blueprint
app.register_blueprint(api_form)
