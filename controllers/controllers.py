from flask import redirect, render_template, url_for, flash, request, session
from flask_wtf import FlaskForm
from app import app, db
from models.forms import LoginForm, PrestamoForm, ReporteForm
from models.models import Usuario, Prestamo
from models.credito import Credito
from controllers.service import Calculadora
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from wtforms_sqlalchemy.fields import QuerySelectField

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    context = {
        'form': form
    }
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Usuario(usuario_nombre=form.username.data, usuario_password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Nuevo usuario creado')
        return redirect(url_for('index'))
    return render_template('signup.html', **context)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    context = {
        'form': form
    }
    if form.validate_on_submit():
        user = Usuario.query.filter_by(usuario_nombre=form.username.data).first()
        if user:
            if check_password_hash(user.usuario_password, form.password.data):
                login_user(user)
                if user.usuario_role == 1:
                    return redirect(url_for('banco'))
                return redirect(url_for('cliente'))
        return 'invalid username or password'
    return render_template('login.html', **context)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@login_required
def cliente_query():
    name = current_user.usuario_nombre
    return Prestamo.query.filter_by(usuario_nombre=name)

class ClienteForm(FlaskForm):
    opts = QuerySelectField(query_factory=cliente_query, allow_blank=False)

@app.route('/cliente', methods=['GET', 'POST'])
@login_required
def cliente():
    name = current_user.usuario_nombre
    data = []
    is_prestamo = False
    form2 = None
    flag = False
    usuario = Prestamo.query.filter_by(usuario_nombre=name).first()
    if usuario != None:
        form2 = ClienteForm()
        flag = True
    if request.method == 'POST' and form2.validate_on_submit:
        monto = form2.opts.data.prestamo_monto
        interes = form2.opts.data.prestamo_interes
        plazo = form2.opts.data.prestamo_plazo
        prestamo = Credito(monto,interes,plazo)
        session['monto'] = monto
        session['interes'] = interes
        session['plazo'] = plazo
        data = Calculadora.alemana(prestamo)
        is_prestamo = True
        return render_template('cliente.html', is_prestamo=is_prestamo, data=data, name=name, form2=form2, flag=flag)
    return render_template('cliente.html', is_prestamo=is_prestamo, data=data, name=name, form2=form2, flag=flag)

@app.route('/banco', methods=['GET', 'POST'])
@login_required
def banco():
    name = current_user.usuario_nombre
    form = PrestamoForm()
    context = {
        'name': name,
        'form': form
    }
    if request.method == 'POST':
        if form.validate_on_submit:
            new_prestamo = Prestamo(prestamo_monto=form.monto.data, prestamo_interes=form.interes.data, prestamo_plazo=form.plazo.data, usuario_nombre=form.nombre.data)
            db.session.add(new_prestamo)
            db.session.commit()
            flash('Nuevo prestamo creado')
    return render_template('banco.html', **context)

@app.route('/reporte', methods=['GET', 'POST'])
@login_required
def reporte():
    monto = float(session.get('monto'))
    interes = float(session.get('interes'))
    plazo = int(session.get('plazo'))
    form = ReporteForm()
    data = []
    if request.method == 'POST':
        if form.validate_on_submit():
            prestamo = Credito(monto,interes,plazo)
            valor1 = form.valor_inicio.data
            valor2 = form.valor_fin.data
            data = Calculadora.reporte(valor1,valor2,prestamo)
    return render_template('reporte.html', form=form, data=data)