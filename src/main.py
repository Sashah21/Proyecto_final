from flask import Flask, jsonify, request, render_template
import users, methods


app = Flask(__name__)

#Root/lista de usuarios
@app.route('/')
def root():
    return render_template('menu.html'), 200

@app.route("/users",methods = ['GET'])
def lista_usuarios():
    usuarios = users.cargar_lista_usuarios()
    return render_template('table.html',usuarios = usuarios), 200

@app.route("/users/<int:user_id>",methods = ['GET'])
def editar_usuarios(user_id):
    usuarios = users.cargar_lista_usuarios()
    datos:dict = None
    for usuario in usuarios:
        if usuario['id'] == user_id:
            datos = usuario
    if datos: return jsonify(datos)
    else: return "No hay datos a mostrar"
#lista de usuarios (json)
@app.route('/users/json')
def get_user():
    return jsonify(users.cargar_lista_usuarios()), 200

#Formulario
@app.route('/form', methods = ['GET','POST'])
def formulario_usuario():
    if request.method == 'GET':
        return render_template('form.html'), 200
    if request.method == 'POST':
        #Valores del formulario
        usuario = { "nombre" : request.form.get('nombre'),
                    "apellidos" : request.form.get('apellidos'),
                    "email" : request.form.get('email'),
                    "contraseña" : request.form.get('contraseña'),
                    "telefono" : request.form.get('tfno'),
                    "edad" : request.form.get('edad')}
        try:
            #Guardar usuario
            methods.confirmar_usuario(usuario)
            users.guardar_usuario(usuario)
            return lista_usuarios()
        except ValueError:
            #Error en los valores insertados en el formulario
            error_mensaje = 'Alguno de los campos esta incorrecto.'
            return render_template('form.html', error = error_mensaje)

@app.route('/pruebas')
def pruebas():
    return jsonify(users.cargar_lista_usuarios()), 200


if __name__ == '__main__':
    app.run(debug=True)

