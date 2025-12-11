from flask import Flask, redirect, render_template, request, flash, url_for, session, make_response
import mysql.connector, hashlib


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
    ##cifrarda = hashlib.sha512(contraseña_gerente.encode("utf-8")).hexdigest() 
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
    
    elif(confirmar_contraseña_gerente != contraseña_gerente): 
        return render_template("registro_gerente.html", incorrectas = "Las contraseñas no coinciden")
    
    else:
        return render_template("registro_gerente.html", msg0 = "credenciales incorrectas")


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
        return render_template("registro_usuario.html", msg = "La contraseña no es la misma que en confirmar contraseña juan estupido")



@programa.route("/")
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
                return redirect("/interfaz_principal_g")
            else:
                return render_template("login.html", msg1 = "Credenciales de usuario no reconocido.")  
            
    else:
        return render_template("login.html" ,msg="Credenciales incorrectas. Inténtalo de nuevo."  )


@programa.route("/interfaz_principal_g")
def interf_principal():
    cursor = my_db.cursor()
    cursor.execute("SELECT id, nombre, categoria, cantidad, fecha_ingreso FROM bebidas")
    productos = cursor.fetchall()
    return render_template("interfaz_principal_gerente.html", productos=productos)

@programa.route("/productos")
def mostrar_productos():
    cursor = my_db.cursor()
    cursor.execute("SELECT id, nombre, categoria, cantidad, fecha_ingreso FROM bebidas")
    productos = cursor.fetchall()
    return render_template("productos.html", productos=productos )


@programa.route("/agrega_producto")
def agregar_producto():
    return render_template("agregar_producto.html")


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


@programa.route("/categorias")
def mostrar_categoria():
    cursor = my_db.cursor()
    cursor.execute("SELECT nombre_categoria FROM categorias")
    categorias = cursor.fetchall()
    return render_template("categorias.html", categorias = categorias)

@programa.route("/crear_categoria")
def agregar_categoria():
    return render_template("crear_categoria.html")

@programa.route("/crear_categoria", methods = ["POST"])
def insertar_categoria():
    crear_nueva_categoria = request.form["crear_nueva_categoria"]
    cursor = my_db.cursor()
    sql = f"SELECT nombre_categoria FROM categorias WHERE nombre_categoria = '{crear_nueva_categoria}'"
    cursor.execute(sql)
    resultado = cursor.fetchone()
    
    if resultado:
        # Ya existe → enviar mensaje
        mensaje = "La categoría ya existe"
        return render_template("crear_categoria.html", mensaje=mensaje)
    
    else:
        cursor = my_db.cursor()
        sql = f"INSERT INTO categorias (nombre_categoria) VALUES ('{crear_nueva_categoria}')"
        cursor.execute(sql)
        my_db.commit()
        return redirect("/interfaz_principal_g")
    
        


@programa.route("/cavas_bodegas")
def cavas_bodegas():
    return render_template("cavas_bodegas.html")


@programa.route("/movimientos")
def movimientos():
    return render_template("movimientos.html")


@programa.route("/empleados")
def empleados():
    cursor = my_db.cursor()
    cursor.execute("SELECT num_id, nom_comple, correo, num_tel, fecha_naci, tipo_id FROM usuarios WHERE roll = '2'")
    empleados = cursor.fetchall()
    
    return render_template("empleados.html" , empleados=empleados)


@programa.route("/proveedores")
def mostrar_proveedores():
    cursor = my_db.cursor()
    cursor.execute("SELECT cedula, nit, nombre, telefono, correo, direccion FROM proveedores")
    proveedores = cursor.fetchall()
    return render_template("proveedores.html", proveedores = proveedores )


@programa.route("/agregar_proveedor")
def a_proveedores():
    return render_template("agregar_proveedor.html")


@programa.route("/agregar_proveedor", methods = ["POST"])
def registro_proveedor():
    nit_empresa_proveedor = request.form["nit_empresa_proveedor"]
    nombre_proveedor = request.form["nombre_proveedor"]
    correo_proveedor = request.form["correo_proveedor"]
    id_proveedor = request.form["id_proveedor"]
    telefono_proveedor = request.form["telefono_proveedor"]
    direccion_empresa_proveedor = request.form["direccion_empresa_proveedor"]
    cursor = my_db.cursor()
    
    #aqui agrego el producto
    sql = f"INSERT INTO proveedores (cedula, nit, nombre, telefono, correo, direccion ) VALUES ('{id_proveedor}' , '{nit_empresa_proveedor}' , '{nombre_proveedor}' , '{telefono_proveedor}' , '{correo_proveedor}' , '{direccion_empresa_proveedor}')"
    cursor.execute(sql)
    my_db.commit()
    
    #esta parte muestra los productos
    cursor.execute("SELECT cedula, nit, nombre, telefono, correo, direccion FROM proveedores ")
    proveedores = cursor.fetchall()
    
    
    return render_template("proveedores.html" , proveedores = proveedores)

@programa.route("/principal")
def principal():
    return render_template("interfaz_principal_gerente.html")


@programa.route("/reportes")
def reportes():
    return render_template("reportes.html")


@programa.route("/cerrar_sesion")
def cerrar_sesion():
    session.clear()
    return redirect("/")









    
if __name__=="__main__":
    programa.run(debug=True, port=5080)