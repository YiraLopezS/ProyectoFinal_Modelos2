from flask import Flask, request, render_template, make_response, session, url_for, redirect
from flask_wtf import CSRFProtect
import forms
from flask_mysqldb import MySQL

app= Flask(__name__)
app.secret_key= 'la_clave_de_Pepito'
csrf= CSRFProtect(app)

app.config['MySQL_HOST']= 'localhost'
app.config['MySQL_USER']= 'yira'
app.config['MySQL_PASSWORD']= 'yira'
app.config['MySQL_DB'] = 'pagina_juegos'
app.config['MySQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def index():
	if 'user' in session:
		username = session['user']
		print (username)
	else: return redirect(url_for('login'))
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	loginForm= forms.LoginForm(request.form)
	if (request.method=='POST' and loginForm.validate()):
		session['user'] = loginForm.user.data
		session['password']=loginForm.password.data
		usuario = request.form['user']
		password = request.form['passsword']
		cur = mysql.connetion.cursor()
		cur.execute('INSERT INTO pagina_juegos (usuario,password) VALUES (%s,%s)', (usuario,password))
		mysql.connetion.commit()
	if 'user' in session:
		return redirect(url_for('index'))
	return render_template('login.html', form=loginForm)

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
	
@app.route('/juegoSalt')
def juego3():
	return render_template('Saltarin.html')
	
@app.route('/juegoBuscF')
def juego4():
	return render_template('BuscF.html')
	
@app.route('/juegoGalaga')
def juego5():
	return render_template('Galaga.html')

if __name__=='__main__':
	app.run(debug=True,port=8000)
