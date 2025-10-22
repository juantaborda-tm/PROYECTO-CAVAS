from flask import Flask, redirect, render_template, request
import mysql.connector

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
    nit_empresa = request.form["nit_empresa"]
    fecha_nacimiento_g = request.form["fecha_nacimiento_g"]
    id_gerente = request.form["id_gerente"]
    email_gerente = request.form["email_gerente"]
    cursor = my_db.cursor()
    sql = f"INSERT INTO usuarios (nombre_empresa, nombre, identificacion, fecha_nacimiento_g, telefono, contraseña, nit_empresa, id_gerente, email_gerente) VALUE('{nombre_empresa}', '{nit_empresa}','{nombre_gerente}', '{fecha_nacimiento_g}','{id_tipo_gerente}', {id_gerente}', '{tel_gerente}','{email_gerente}' '{contraseña_gerente}', )"
    cursor.execute(sql)
    my_db.commit()
    return redirect("/")





if __name__=="__main__":
    programa.run(debug=True, port=5080)
