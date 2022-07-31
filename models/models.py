from app import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_role = db.Column(db.Integer)
    usuario_nombre = db.Column(db.String(100), nullable=False, unique=True)
    usuario_password = db.Column(db.String(100), nullable=False)
    prestamos = db.relationship('Prestamo', backref='usuario')
    def get_id(self):
        return self.id

class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prestamo_monto = db.Column(db.Numeric(9,2), nullable=False)
    prestamo_interes = db.Column(db.Numeric(9,2), nullable=False)
    prestamo_plazo = db.Column(db.Integer, nullable=False)
    usuario_nombre = db.Column(db.String(100), db.ForeignKey('usuario.usuario_nombre'))
    def __repr__(self):
        return 'Préstamo de: {}'.format(self.prestamo_monto)

db.create_all()