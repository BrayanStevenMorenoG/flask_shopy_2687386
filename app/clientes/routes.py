from app.clientes import clientes
from flask import render_template, redirect , flash
from flask_login import login_required
from .forms  import NewClientForm, EditClientForm
import app

@clientes.route('/crear',  methods = ['GET', 'POST'])
def crear():
        cliente = app.models.Cliente()
        form = NewClientForm()
        if form.validate_on_submit():
            # Guarda el cliente en la bd
            form.populate_obj(cliente),
            app.db.session.add(cliente),
            app.db.session.commit()
            flash('CLiente registrado correctamente')
            return redirect('/clientes/listar')
        return render_template('crear.html', form = form)

@clientes.route("/listar")
@login_required
def listar():
     clientes = app.models.Cliente.query.all()
     return render_template("listarusu.html", clientes = clientes)


@clientes.route('editar/<cliente_id>', methods = ['GET', 'POST'])
def editar(cliente_id):
    cliente = app.models.Cliente.query.get(cliente_id)
    form =  EditClientForm(obj = cliente)
    if form.validate_on_submit():
        form.populate_obj(cliente),
        app.db.session.commit()
        flash("Cliente actualizado correctamente")
        return redirect('/clientes/listar')
    return render_template('crear.html', form = form)

@clientes.route('eliminar/<cliente_id>')
def eliminar(cliente_id):
    cliente = app.models.Cliente.query.get(cliente_id)
    if cliente:
         app.db.session.delete(cliente)
         app.db.session.commit()
         flash("Producto eliminado correctamente")
    return redirect('/clientes/listar')

