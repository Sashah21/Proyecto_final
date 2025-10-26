from flask import Flask, jsonify, request, render_template, url_for, redirect
import users, methods

app = Flask(__name__)

#Menu
@app.route('/')
def root():
    return render_template('menu.html'), 200
#Lista de usuarios
@app.route("/users",methods = ['GET','POST'])
def lista_usuarios():
    #Variables
    args = request.args.to_dict()
    usuarios = users.cargar_lista_usuarios()
    if not args:
        return render_template('table.html',usuarios = usuarios)
    #Variables generales(Diferentes acciones en la lista)
    metodo = args.get('method')
    usuario = args.get('user')
    confirmar = args.get('confirm')
    #Logica edit
    if metodo == 'edit' and usuario: #Metodo editar y asegurarse de que hay usuario
        usuario_editado = users.obtener_usuario(int(usuario))
        if confirmar: #Sobreescribe y guarda el usuario
            campos = ["nombre","apellidos","email","contraseña","telefono","edad","id"]
            for campo in campos:
                if args.get(campo): usuario_editado[campo] = args[campo]
            try:
                methods.confirmar_usuario(usuario_editado,reescribir=True)
                users.modificar_usuario(usuario_editado)
            except ValueError:
                return render_template('table.html', usuarios = usuarios, edit_user = int(usuario), error = 'e')
            return redirect(url_for('lista_usuarios'))
        return render_template('table.html',usuarios = usuarios, edit_user = int(usuario))
    #Logica delete
    elif metodo == 'delete' and usuario: #Metodo eliminar y asegurarse de que hay usuario
        if confirmar:
            users.eliminar_usuario(int(usuario))
            return redirect(url_for('lista_usuarios'))
        return render_template('table.html', usuarios = usuarios, delete_user = int(usuario))
    
    return render_template('table.html',usuarios = usuarios)

#lista de usuarios (json)
@app.route('/users/json')
def usuarios_json():
    return jsonify(users.cargar_lista_usuarios()), 200
#Formulario
@app.route('/form', methods = ['GET','POST'])
def formulario_usuario():
    if request.method == 'GET':
        return render_template('form.html'), 200
    if request.method == 'POST':
        #Valores del formulario
        usuario = request.form.to_dict()
        try:
            #Guardar usuario
            methods.confirmar_usuario(usuario)
            users.guardar_usuario_nuevo(usuario)
            return lista_usuarios()
        except ValueError:
            #Error en los valores insertados en el formulario
            error_mensaje = 'Alguno de los campos esta incorrecto.'
            return render_template('form.html', error = error_mensaje)

if __name__ == '__main__':
    app.run(debug=True)

