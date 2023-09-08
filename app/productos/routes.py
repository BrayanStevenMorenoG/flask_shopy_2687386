from app.productos import productos
from flask import render_template, redirect , flash
from .forms  import NewProductForm, EditProductForm
import app
import os


@productos.route('/crear',  methods = ['GET', 'POST'])
def crear():        
        producto = app.models.Producto()
        form = NewProductForm()
        if form.validate_on_submit():
            # Guarda el producto en la bd
            form.populate_obj(producto),
            producto.imagen = form.Imagen.data.filename
            app.db.session.add(producto),
            app.db.session.commit()
            #Subir imagen a /imagenes
            archivo = form.Imagen.data 
            archivo.save(os.path.abspath(os.getcwd() + "\\app\\productos\\imagenes\\"+ producto.imagen))
            flash('Producto registrado correctamente')
            return redirect('/productos/listar')
        return render_template('crear.html', form = form)

@productos.route('/listar')
def listar():
    # Seleccionar los productos
    productos = app.models.Producto.query.all()
    return render_template("listar.html", productos = productos)

@productos.route('editar/<producto_id>', methods = ['GET', 'POST'])
def editar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    form =  EditProductForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p),
        app.db.session.commit()
        flash("Producto actualizado correctamente")
        return redirect('/productos/listar')
    return render_template('crear.html', form = form)

@productos.route('eliminar/<producto_id>')
def eliminar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    if p:
         app.db.session.delete(p)
         app.db.session.commit()
         flash("Producto eliminado correctamente")
    return redirect('/productos/listar')

