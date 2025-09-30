from flask import Flask,jsonify,request,render_template
import users


app = Flask(__name__)


@app.route('/')
def root():
    return render_template('root.html')

#Metodo get
@app.route('/users/<user_id>')
def get_user(user_id):
    user = {'id':user_id,'name':'Test','telefono':'999-666-333'}
    query = request.args.get('query')
    if query:
        user['query'] = query
    return jsonify(user), 200

#Metodo post
@app.route('/form', methods = ['GET','POST'])
def formulario_usuario():
    if request.method == 'GET':
        return render_template('form.html'), 200
    elif request.method == 'POST':
        pass
    data = request.get_json()
    data['status'] = 'User created'
    return jsonify(data), 201



#Lista de usuarios
@app.route("/users",methods = ['GET'])
def lista_usuarios():
    usuarios = users.cargar_lista_usuarios()
    return render_template('user_table.html',usuarios = usuarios), 200


if __name__ == '__main__':
    app.run(debug=True)

