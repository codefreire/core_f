from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor1234@localhost/banco_db'
app.secret_key = os.urandom(32)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)

from controllers.controllers import *
from models.admin import *

if __name__ == '__main__':
    app.run(debug=True)