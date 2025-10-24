from flask import Flask, redirect, render_template, request
import mysql.connector, django

my_db = mysql.connector.connect(host = "localhost",
                                port = "3306",
                                user = "root",
                                password = "",
                                database = "cavas")

programa = Flask(__name__)


#Primero registrar el gerente

@programa.route("/")
def registro_gerente():
    return render_template("registro_gerente.html")


@programa.route("/", methods = ["POST"])
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
    roll = "1" #roll 1 es gerente
    cursor = my_db.cursor()
    #corregir orden de sintaxys SQL
    sql = f"INSERT INTO usuarios (num_id, nom_comple, correo, contra, nom_empresa, num_tel, nit_empre, fecha_naci, tipo_id, roll) VALUES ('{id_gerente}' , '{nombre_gerente}' , '{email_gerente}' , '{contraseña_gerente}' , '{nombre_empresa}' , '{tel_gerente}' , '{nit_emprese}' , '{fecha_nacimiento_g}' , '{id_tipo_gerente}' , '{roll}')"
    cursor.execute(sql)
    my_db.commit()
    return render_template("registro_gerente.html")


@programa.route("/registro_u")








if __name__=="__main__":
    programa.run(debug=True, port=5080)
