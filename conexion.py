from tkinter.tix import Tk
from flask import Flask, flash, redirect, render_template, request
import mysql.connector, django
import os 
from datetime import datetime, timedelta


my_db = mysql.connector.connect(host = "localhost",
                                port = "3306",
                                user = "root",
                                password = "",
                                database = "cavas")

programa = Flask(__name__)
programa.permanent_session_lifetime = timedelta(seconds=60)  # Duración de sesión



#Primero registrar el gerente




@programa.route("/registro_gerente")
def registro_gerente():
    return render_template("registro_gerente.html")

@programa.route("/registro_gerente", methods = ["POST"])
def registro_g():
    nombre_empresa = request.form["nombre_empresa"]
    nombre_gerente = request.form["nombre_gerente"]
    id_tipo_gerente = request.form["id_tipo_gerente"]
    tel_gerente = request.form["tel_gerente"]
    contraseña_gerente = request.form["contraseña_gerente"]
    nit_emprese = request.form["nit_empresa"]
    fecha_nacimiento_g = request.form["fecha_nacimiento_g"]
    id_gerente = request.form["id_gerente"]
    email_gerente = request.form["email_gerente"]
    confirmar_contraseña_gerente = request.form["confirmar_contraseña_gerente"] #Confirmar contraseña
    roll = "1" #roll 1 es gerente
    cursor = my_db.cursor()
    #mensaje en ventana flotante  
    
    if (contraseña_gerente != confirmar_contraseña_gerente):
        flash("Las contraseñas no coinciden")
        return render_template("registro_gerente.html")
    
    elif (contraseña_gerente == confirmar_contraseña_gerente):
        cursor = my_db.cursor()
        sql = f"INSERT INTO usuarios (num_id, nom_comple, correo, contra, num_tel, fecha_naci, tipo_id, roll) VALUES ('{id_gerente}' , '{nombre_gerente}' , '{email_gerente}' , '{contraseña_gerente}' , '{tel_gerente}' , '{fecha_nacimiento_g}' , '{id_tipo_gerente}' , '{roll}')"
        cursor.execute(sql)
        my_db.commit()
        return render_template("registro_gerente.html")
    
    else:
        return ("Algo ocurrio, intentalo de nuevo")
    

#Luego registrar usuarios 

@programa.route("/registro_usuarios")
def registro_usuarios():
    return render_template("registro_usuario.html")

@programa.route("/registro_usuarios", methods = ["POST"])
def registro_u():
    nombre_usuario = request.form["nombre_usuario"]
    id_tipo_usuario = request.form["id_tipo_usuario"]
    tel_usuario = request.form["tel_usuario"]
    contraseña_usuario = request.form["contraseña_usuario"]
    fecha_usuario = request.form["fecha_usuario"]
    id_usuario = request.form["id_usuario"]
    email_usuario = request.form["email_usuario"]
    confirmar_contraseña_usuario = request.form["confirmar_contraseña_usuario"] #Confirmar contraseña
    roll = "2" #roll 2 es usuario normal
    cursor = my_db.cursor() 
    
    if (contraseña_usuario != confirmar_contraseña_usuario):
        return ("Las contraseñas no coinciden")
    
    elif (contraseña_usuario == confirmar_contraseña_usuario):
        cursor = my_db.cursor()
        sql = f"INSERT INTO usuarios (num_id, nom_comple, correo, contra, num_tel, fecha_naci, tipo_id, roll) VALUES ('{id_usuario}' , '{nombre_usuario}' , '{email_usuario}' , '{contraseña_usuario}' , '{tel_usuario}' , '{fecha_usuario}' , '{id_tipo_usuario}' , '{roll}')"
        cursor.execute(sql)
        my_db.commit()
        return render_template("registro_usuario.html")
    
    else:
        return ("Algo ocurrio, intentalo de nuevo")



if __name__=="__main__":
    programa.run(debug=True, port=5080)
