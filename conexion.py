<<<<<<< HEAD
from flask import Flask, redirect, render_template, request, flash, url_for
import mysql.connector  
from tkinter import *
from tkinter import messagebox  

=======
from flask import Flask, redirect, render_template, request
import mysql.connector
>>>>>>> 22a8f39ec90da2391888169bd00174c2a36c975a

my_db = mysql.connector.connect(host = "localhost",
                                port = "3306",
                                user = "root",
                                password = "",
                                database = "cavas")

programa = Flask(__name__)
<<<<<<< HEAD
programa.secret_key = 'alan123'

#funcion para mostrar ventana de registro
=======

>>>>>>> 22a8f39ec90da2391888169bd00174c2a36c975a

#Primero registrar el gerente


<<<<<<< HEAD

@programa.route("/registro_gerente")
def registro_gerente():
    return render_template("registro_gerente.html")

@programa.route("/registro_gerente", methods = ["POST"])
=======
@programa.route("/")
def registro_gerente():
    return render_template("registro_gerente.html")

@programa.route("/", methods = ["POST"])
>>>>>>> 22a8f39ec90da2391888169bd00174c2a36c975a
def registro_g():
    nombre_empresa = request.form["nombre_empresa"]
    nombre_gerente = request.form["nombre_gerente"]
    id_tipo_gerente = request.form["id_tipo_gerente"]
    tel_gerente = request.form["tel_gerente"]
    contraseña_gerente = request.form["contraseña_gerente"]
<<<<<<< HEAD
    confirmar_contraseña_gerente = request.form["confirmar_contraseña_gerente"]
=======
>>>>>>> 22a8f39ec90da2391888169bd00174c2a36c975a
    nit_emprese = request.form["nit_empresa"]
    fecha_nacimiento_g = request.form["fecha_nacimiento_g"]
    id_gerente = request.form["id_gerente"]
    email_gerente = request.form["email_gerente"]
    roll = "1" #roll 1 es gerente
<<<<<<< HEAD
    #corregir orden de sintaxys SQL
    
    if(confirmar_contraseña_gerente == contraseña_gerente):
        cursor = my_db.cursor()
        sql = f"INSERT INTO usuarios (num_id, nom_comple, correo, contra, nom_empresa, num_tel, nit_empre, fecha_naci, tipo_id, roll) VALUES ('{id_gerente}' , '{nombre_gerente}' , '{email_gerente}' , '{contraseña_gerente}' , '{nombre_empresa}' , '{tel_gerente}' , '{nit_emprese}' , '{fecha_nacimiento_g}' , '{id_tipo_gerente}' , '{roll}')"
        cursor.execute(sql)
        my_db.commit()
        return render_template("registro_gerente.html")
    
    else: 
        return render_template("registro_gerente.html", msg = "La contraseña no coincide")
=======
    cursor = my_db.cursor()
    #corregir orden de sintaxys SQL
    sql = f"INSERT INTO usuarios (num_id, nom_comple, correo, contra, nom_empresa, num_tel, nit_empre, fecha_naci, tipo_id, roll) VALUES ('{id_gerente}' , '{nombre_gerente}' , '{email_gerente}' , '{contraseña_gerente}' , '{nombre_empresa}' , '{tel_gerente}' , '{nit_emprese}' , '{fecha_nacimiento_g}' , '{id_tipo_gerente}' , '{roll}')"
    cursor.execute(sql)
    my_db.commit()
    return render_template("registro_gerente.html")
>>>>>>> 22a8f39ec90da2391888169bd00174c2a36c975a


#Luego registrar usuarios 

<<<<<<< HEAD
@programa.route("/registro_usuario")
def registro_usuarios():
    return render_template("registro_usuario.html")

@programa.route("/registro_usuarios", methods = ["POST"])
=======
@programa.route("/registro_user")
def registro_gerente():
    return render_template("registro_gerente.html")

@programa.route("/registro_user", methods = ["POST"])
>>>>>>> 22a8f39ec90da2391888169bd00174c2a36c975a
def registro_u():
    nombre_usuario = request.form["nombre_usuario"]
    id_tipo_usuario = request.form["id_tipo_usuario"]
    tel_usuario = request.form["tel_usuario"]
    contraseña_usuario = request.form["contraseña_usuario"]
<<<<<<< HEAD
    confirmar_contraseña_usuario = request.form["confirmar_contraseña_usuario"]
=======
>>>>>>> 22a8f39ec90da2391888169bd00174c2a36c975a
    fecha_usuario = request.form["fecha_usuario"]
    id_usuario = request.form["id_usuario"]
    email_usuario = request.form["email_usuario"]
    roll = "2" #roll 2 es usuario normal
<<<<<<< HEAD
    if(confirmar_contraseña_usuario == contraseña_usuario):
        cursor = my_db.cursor()
        sql = f"INSERT INTO usuarios (num_id, nom_comple, correo, contra, num_tel, fecha_naci, tipo_id, roll) VALUES ('{id_usuario}' , '{nombre_usuario}' , '{email_usuario}' , '{contraseña_usuario}' , '{tel_usuario}' , '{fecha_usuario}' , '{id_tipo_usuario}' , '{roll}')" 
        cursor.execute(sql)
        my_db.commit()
        return render_template("registro_usuario.html")
    else: 
        return render_template("registro_usuario.html", msg = "La contraseña no coincide")



@programa.route("/login")
def login():
    return render_template("login.html")

@programa.route("/login", methods = ["POST"])
def logear():
    email_usuario = request.form["email_usuario"]
    contraseña_usuario = request.form["contraseña_usuario"]
    cursor = my_db.cursor()
    sql = f"SELECT * FROM usuarios WHERE correo = '{email_usuario}' AND contra = '{contraseña_usuario}'"
    cursor.execute(sql)   
    resultado = cursor.fetchone()
    
    if (resultado):
        sql = f"SELECT roll FROM usuarios WHERE correo = '{email_usuario}' AND contra = '{contraseña_usuario}'"
        cursor.execute(sql)
        resultado_roll = cursor.fetchone()
        if resultado_roll:
            roll = resultado_roll[0]
            if roll == "1":
                return render_template("interf_geren.html")
            elif roll == "2":
                return render_template("interf_user.html")
            else:
                return render_template("login.html", msg="Credenciales de usuario no reconocido.")
            
    else:
        return render_template("login.html", msg="Credenciales incorrectas. Inténtalo de nuevo.")



@programa.route("/principal")
def principal():
    return render_template("interfaz_principal.html")

=======
    cursor = my_db.cursor() 
    sql = f"INSERT INTO usuarios (num_id, nom_comple, correo, contra, num_tel, fecha_naci, tipo_id, roll) VALUES ('{id_usuario}' , '{nombre_usuario}' , '{email_usuario}' , '{contraseña_usuario}' , '{tel_usuario}' , '{fecha_usuario}' , '{id_tipo_usuario}' , '{roll}')"
    return render_template("registro_usuario.html")



>>>>>>> 22a8f39ec90da2391888169bd00174c2a36c975a

if __name__=="__main__":
    programa.run(debug=True, port=5080)
