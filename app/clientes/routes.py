from flask import render_template, redirect, flash
from . import clientes 
import app 
from .forms import NewClienteForm, EditClienteForm
import os 

#rutas del modulo "clientes"
@clientes.route("/listar")
def listar():
    #Se listan los clientes
    #modelos
    clientes = app.models.Cliente.query.all()
    return render_template ("listar.html",
                            clientes = clientes)
    
@clientes.route("/crear" , 
                 methods =["GET", "POST"])
def nuevo():
    #Registrar formulario
    form = NewClienteForm()
    c = app.models.Cliente()
    if form.validate_on_submit():
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
        
        flash("Cliente registrado correctamente")
        return redirect("/clientes/listar")
        
    return render_template("crear.html",
                           operacion = "Nuevo",
                           form = form)
    
@clientes.route("/actualizar/<cliente_id>",
                 methods =['GET' , 'POST'])
def editar (cliente_id):
    c = app.models.Cliente.query.get(cliente_id)
    form = EditClienteForm(obj = c)
    if form.validate_on_submit():
        form.populate_obj(c)
        app.db.session.commit()
        flash("Cliente actualizado correctamente")
        return redirect("/clientes/listar")
        
    return render_template("crear.html",
                           operacion = "Actualizar",
                           form=form ) 
    

@clientes.route('/eliminar/<clientes_id>')
def eliminar(clientes_id):
    c = app.models.Cliente.query.get(clientes_id)
    app.db.session.delete(c)
    app.db.session.commit()
    flash("Cliente eliminado correctamente")
    return redirect("/clientes/listar")