from wtforms import Form, StringField, TextField, validators, PasswordField
from wtforms.fields.html5 import EmailField

class CommentForm(Form):

	user= StringField('usuario', 
		[
			validators.Required('Ingrese un unsuario'),
			validators.length(min=3,max=25,message='Ingrese un usuario que tenga de 3 a 25 caracteres')
		])
	email= EmailField('Correo',
		[
			validators.Required('Ingrese un e-mail'),
			validators.Email(message='Email invalido')
		])
	comment=TextField('Comentario')
class LoginForm(Form):
	user= StringField('usuario', 
		[
			validators.Required('Ingrese un unsuario'),
			validators.length(min=3,max=25,message='Ingrese un usuario que tenga de 3 a 25 caracteres')
		])
	password = PasswordField('Password', [validators.Required(message='Se requiere contraseña')])