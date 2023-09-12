from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, NumberRange, Email, Length


class ClienteForm():
    username = StringField("Nombre del usuario", validators = [InputRequired(message="Nombre de usuario requerido")])
    email = StringField("Email", validators = [InputRequired(message="Email requerido"), Email("Debe ser email")])
    password = StringField("Contraseña", validators = [Length(min=10, max=17)])
    
    
class NewClienteForm(FlaskForm, ClienteForm):    
    submit = SubmitField("Guardar")
    
class EditClienteForm(FlaskForm, ClienteForm):
    submit = SubmitField("Actualizar")