from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, NumberRange



class RegistrarProductoForm(FlaskForm):
    nombre = StringField("nombre del producto", validators = [InputRequired(message="Nombre del producto requerido")])
    precio = IntegerField("Precio del producto", validators= [InputRequired(message="Precio del producto requerido"), 
                                                              NumberRange(  message="Precio fuera de rango",
                                                              min = 10,
                                                              max = 100000
                                                            )])
    imagen = FileField("Seleccione imagen del producto:", validators = [FileRequired(message= "Debe seleccionar una imagen"), 
                                                                        FileAllowed([ 'jpg','png'], "Solo se permiten carga de imagenes" )
                                                                        ])
    submit = SubmitField("Guardar")