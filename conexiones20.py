from flask import Flask, redirect, render_template, request, flash, url_for, session
import mysql.connector  


my_db = mysql.connector.connect(host = "localhost",
                                port = "3306",
                                user = "root",
                                password = "",
                                database = "cavas")

programa = Flask(__name__)
programa.secret_key = 'alan123'

#funcion para mostrar ventana de registro

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
    confirmar_contraseña_gerente = request.form["confirmar_contraseña_gerente"]
    nit_emprese = request.form["nit_empresa"]
    fecha_gerente = request.form["fecha_gerente"]
    id_gerente = request.form["id_gerente"]
    email_gerente = request.form["email_gerente"]
    roll = "1" #roll 1 es gerente
    #corregir orden de sintaxys SQL
    
    if(confirmar_contraseña_gerente == contraseña_gerente):
        cursor = my_db.cursor()
        sql = f"INSERT INTO usuarios (num_id, nom_comple, correo, contra, nom_empresa, num_tel, nit_empre, fecha_naci, tipo_id, roll) VALUES ('{id_gerente}' , '{nombre_gerente}' , '{email_gerente}' , '{contraseña_gerente}' , '{nombre_empresa}' , '{tel_gerente}' , '{nit_emprese}' , '{fecha_gerente}' , '{id_tipo_gerente}' , '{roll}')"
        cursor.execute(sql)
        my_db.commit()
        return render_template("registro_gerente.html")
    
    else: 
        return render_template("registro_gerente.html", msg = "La contraseña no coincide")


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
    confirmar_contraseña_usuario = request.form["confirmar_contraseña_usuario"]
    fecha_usuario = request.form["fecha_usuario"]
    id_usuario = request.form["id_usuario"]
    email_usuario = request.form["email_usuario"]
    roll = "2" #roll 2 es usuario normal
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
                return redirect("/interfaz_principal_g")
            elif roll == "2":
                return render_template("interf_user.html")
            else:
                return render_template("login.html", msg1 = "Credenciales de usuario no reconocido.")  
            
    else:
        return render_template("login.html", msg="Credenciales incorrectas. Inténtalo de nuevo.")


@programa.route("/interfaz_principal_g")
def interf_principal():
    cursor = my_db.cursor()
    cursor.execute("SELECT id, nombre, categoria, cantidad, fecha_ingreso FROM bebidas")
    productos = cursor.fetchall()
    return render_template("interfaz_principal_gerente.html", productos=productos)


@programa.route("/agrega_producto")
def agregar_producto():
    return render_template("agregar_producto.html")


#Que al agregar un producto mandé eso al backend y muestre en el historial lo que agregó

@programa.route("/agrega_producto", methods = ["POST"])
def agrega_p():
    id_crear_producto = request.form["id_crear_producto"]
    nombre_crear_producto = request.form["nombre_crear_producto"]
    categoria_crear_producto = request.form["categoria_crear_producto"]
    cantidad_crear_producto = request.form["cantidad_crear_producto"]
    cursor = my_db.cursor()
    sql = f"INSERT INTO bebidas (id, nombre, categoria, cantidad) VALUES ('{id_crear_producto}' , '{nombre_crear_producto}' , '{categoria_crear_producto}' , '{cantidad_crear_producto}')"
    cursor.execute(sql)
    my_db.commit()
    cursor.execute("SELECT id, nombre, categoria, cantidad, fecha_ingreso FROM bebidas")
    productos = cursor.fetchall()
    
    return render_template("interfaz_principal_gerente.html", productos=productos)


7
@programa.route("/empleados")
def empleados():
    cursor = my_db.cursor()
    cursor.execute("SELECT num_id, nom_comple, correo, num_tel, fecha_naci, tipo_id FROM usuarios WHERE roll = '2'")
    empleados = cursor.fetchall()
    
    return render_template("empleados.html" , empleados=empleados)


@programa.route("/movimientos")
def movimientos():
    return render_template("movimientos.html")



    
if __name__=="__main__":
    programa.run(debug=True, port=5080)