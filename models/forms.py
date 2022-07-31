from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, DecimalField
from wtforms.validators import Length, InputRequired

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=5, max=100)])

class PrestamoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[InputRequired(), Length(min=4, max=15)])
    monto = DecimalField('Monto', validators=[InputRequired()], places=2)
    interes = DecimalField('Interes', validators=[InputRequired()], places=2)
    plazo = IntegerField('Plazo', validators=[InputRequired()])

class PagoForm(FlaskForm):
    pago = DecimalField('Ingrese dinero', validators=[InputRequired()], places=2)

class ReporteForm(FlaskForm):
    valor_inicio = DecimalField('Valor mínimo cuota', validators=[InputRequired()], places=2)
    valor_fin = DecimalField('Valor máximo cuota', validators=[InputRequired()], places=2)