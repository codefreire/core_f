from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from .models import *

admin = Admin(app)
admin.add_view(ModelView(Usuario, db.session))
admin.add_view(ModelView(Prestamo, db.session))