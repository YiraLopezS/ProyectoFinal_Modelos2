from flask import Flask, request, render_template, make_response, session, url_for, redirect
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms

app= Flask(__name__)
app.config.from_object(DevelopmentConfig)
CSRF = CSRFProtect()



@app.route('/')
def index():
	if 'user' in session:
		username = session['user']
		print (username)
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	loginForm= forms.LoginForm(request.form)
	if (request.method=='POST' and loginForm.validate()):
		session['user'] = loginForm.user.data
		
	return render_template('login.html', form=loginForm)

@app.route('/cookie')
def cookie():
	response= make_response(render_template('cookie.html'))
	response.set_cookie('custome_cookie', 'pruebaCookie')
	return response
	
@app.route('/logout')
def logout():
	if 'user' in session:
		session.pop('user')
	return redirect(url_for('login'))

@app.route('/juegoCal')
def juego1():
	return render_template('Calav.html')
	
@app.route('/juegoRun')
def juego2():
	return render_template('CovidRuner.html')

if __name__=='__main__':
	CSRF.init_app(app)
	app.run(port=8000)
