from . import productos
from flask import render_template, redirect, flash
from .forms import NewProductForm, EditProductForm
import app
import os

# Crear rutas del blueprint
@productos.route('/crear', methods=["GET", "POST"])
def crear():
    form = NewProductForm()
    if form.validate_on_submit():
        p = app.models.Producto()
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        flash("Producto registrado con éxito")
        return redirect('/productos/listar')
    return render_template('new.html', form=form)

@productos.route('/listar')
def listar():
    productos = app.models.Producto.query.all()
    return render_template('listar.html', productos=productos)

@productos.route('/editar/<int:producto_id>', methods=['GET', 'POST'])
def editar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    form_edit = EditProductForm(obj=p)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)
        app.db.session.commit()
        flash("Producto editado exitosamente")
        return redirect("/productos/listar")
    return render_template('new.html', form=form_edit)

@productos.route('/eliminar/<int:producto_id>', methods=['GET', 'POST'])
def eliminar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Producto eliminado exitosamente")
    return redirect("/productos/listar")
