import re
import emailSender
from flask import Flask, render_template, url_for, session, request, redirect
from flask_mysqldb import MySQL
import os
import hashlib
from flask_mail import Mail, Message

app = Flask(__name__)


# BASE DE DATOS
app.config['MYSQL_USER'] = 'bfe7f8e0a032e0'
app.config['MYSQL_PASSWORD'] = '2c08931d'
app.config['MYSQL_HOST'] = 'us-cdbr-east-04.cleardb.com'
app.config['MYSQL_DB'] = 'heroku_468b22cd0d65a8e'

# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_DB'] = 'iot'

mysql = MySQL(app)


#Configura el objeto
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'p21092002@gmail.com'
app.config['MAIL_PASSWORD'] = 'tetrfegtvagmlirz'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.secret_key = os.urandom(20)

# El puerto debe coincidir con el tipo de seguridad utilizado.
# Si está utilizando STARTTLS con MAIL_USE_TLS = True, luego usar MAIL_PORT = 587.
# Si usa SSL / TLS directamente con MAIL_USE_SSL = True, luego usar MAIL_PORT = 465.
# Habilite STARTTLS o SSL / TLS, no ambos.


# Crea el objeto mail
mail = Mail(app)



@app.route('/')
def index():

    
    cursor = mysql.connection.cursor()
    cursor.execute(""" SELECT * FROM info_iot """)
    dataINFO = cursor.fetchall()
    cursor.close()
    return render_template('index.html', dataINFO = dataINFO, count = len(dataINFO))
 
@app.route('/about')
def about():


    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        temaPrincipal = request.form['temaPrincipal']
        mensaje = request.form['message']
        
        mensajeCompleto = Message('Equipo IOT con ESP32',
                  sender = 'p21092002@gmail.com',
                  recipients = ['patrick.echevarria.d@uni.pe'])

        #Cuerpo del mensaje
        mensajeCompleto.html = emailSender.correo(name, email, temaPrincipal, mensaje)

        #Enviar el mensaje
        mail.send(mensajeCompleto)

    return render_template('contact.html')
 
@app.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        #Encriptando la contraseña
        password = hashlib.new("sha3_512", password.encode())
        password = password.hexdigest()
        
        cursor = mysql.connection.cursor()
        cursor.execute(""" SELECT * FROM usuarios_iot WHERE email = '{0}'  """.format(
            email))  # Conectandome a la base de datos
        data = cursor.fetchall()  # Creando tupla
        cursor.close()

        if data:
            if email == data[0][2] and password == data[0][3]:
                session['username'] = data[0][0] + ' ' + data[0][1]
                return redirect(url_for('welcome', nombre = session['username'], email = email))
            else:
                return 'ESTA MAL TU CONTRA PENDEJO'
        
        else:
            return 'Usuario o Contraseña incorrecta'

    return render_template('login.html')

@app.route('/SignupAdmin', methods =['GET', 'POST'])
def signupAdmin():

    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastName']
        email = request.form['email']
        password = request.form['password']

        #Encriptando la contraseña
        password = hashlib.new("sha3_512", password.encode())
        password = password.hexdigest()

        cursor = mysql.connection.cursor()
        cursor.execute(""" INSERT INTO usuarios_iot (nombre, apellido, email, contrasena) 
        VALUE ('{0}', '{1}', '{2}', '{3}') """.format(name, lastname, email, password))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('welcome', nombre =name + " " + lastname, email = email))

    return render_template('signupAdmin.html')


@app.route('/Bienvenido/<string:nombre>/<string:email> ', methods=['POST', 'GET'])
def welcome(nombre, email):

    if 'username' in session:

        cursor = mysql.connection.cursor()
        cursor.execute(""" SELECT * FROM usuarios_iot WHERE email = '{0}' """.format(email))
        dataUSER = cursor.fetchall() 
            
        cursor.execute(""" SELECT * FROM info_iot """)
        dataINFO = cursor.fetchall()
        cursor.close()

        if request.method == 'POST':

            if request.form['CHANGE'] == 'ADD':

                titulo = request.form['TITTLE']
                informacion = request.form['INFO']
                linkMasInfo = request.form['LINKaux']


                cursor = mysql.connection.cursor()
                cursor.execute(""" INSERT INTO info_iot (titulo, Informacion, linkMasInfo) 
                VALUE ('{0}','{1}','{2}' ) """.format(titulo, informacion, str(linkMasInfo )))
                mysql.connection.commit()
                cursor.close()
            
            if request.form['CHANGE'] == "DELETE":

                positionFORM = request.form["POSITION"]

                cursor = mysql.connection.cursor()
                cursor.execute(""" DELETE FROM info_iot WHERE id = '{0}' """.format(positionFORM))
                mysql.connection.commit()
                cursor.close()

            if request.form['CHANGE'] == "UPDATE":

                positionFORM = request.form["POSITION"]

                titulo = request.form['TITTLE']
                informacion = request.form['INFO']
                linkMasInfo = request.form['LINKaux']

                cursor = mysql.connection.cursor()
                cursor.execute(""" UPDATE info_iot SET titulo = '{0}', 
                Informacion = '{1}', linkMasInfo = '{2}' WHERE id = '{3}' """.format(titulo, informacion, linkMasInfo, positionFORM))
                mysql.connection.commit()
                cursor.close()

            return render_template('welcome.html', dataUSER = dataUSER, dataINFO = dataINFO, count = len(dataINFO))

        

        
        return render_template('welcome.html', dataUSER = dataUSER, dataINFO = dataINFO, count = len(dataINFO))
    else:
        return 'error'




if __name__ == '__main__':
    app.run(debug=True, port = 8000)