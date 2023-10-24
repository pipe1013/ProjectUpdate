from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class ProductForm:
    nombre = StringField('Nombre del servicio:', validators=[InputRequired(message="Nombre requerido")])
    precio = IntegerField('Precio del servicio:', validators=[InputRequired(message="Precio requerido")])
    fecha = IntegerField('Tiempo estimado (en horas):', validators=[InputRequired(message="Tiempo requerido")])
    descripcion = TextAreaField('Descripción del servicio:', validators=[InputRequired(message="Descripción requerida")])

class NewProductForm(FlaskForm):
    nombre = StringField('Nombre del servicio:', validators=[InputRequired(message="Nombre requerido")])
    precio = IntegerField('Precio del servicio:', validators=[InputRequired(message="Precio requerido")])
    fecha = IntegerField('Tiempo estimado (en Dias):', validators=[InputRequired(message="Tiempo requerido")])
    descripcion = TextAreaField('Descripción del servicio:', validators=[InputRequired(message="Descripción requerida")])
    submit = SubmitField("Registrar")

class EditProductForm(FlaskForm):
    nombre = StringField('Nombre del servicio:', validators=[InputRequired(message="Nombre requerido")])
    precio = IntegerField('Precio del servicio:', validators=[InputRequired(message="Precio requerido")])
    fecha = IntegerField('Tiempo estimado (en Dias):', validators=[InputRequired(message="Tiempo requerido")])
    descripcion = TextAreaField('Descripción del servicio:', validators=[InputRequired(message="Descripción requerida")])
    submit = SubmitField("Actualizar")
