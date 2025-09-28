from flask import Flask,jsonify,request,render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('root.html')

#GET (Obtener)
#POST (Crear)
#PUT (actualizar)
#DELETE (Borrar)

#Metodo get
@app.route('/users/<user_id>')
def get_user(user_id):
    user = {'id':user_id,'name':'Test','telefono':'999-666-333'}
    query = request.args.get('query')
    if query:
        user['query'] = query
    return jsonify(user), 200

#Metodo post
@app.route('/users', methods = ['POST'])
def create_user():
    data = request.get_json()
    data['status'] = 'User created'
    return jsonify(data), 201

@app.route("/hello")
def hello():
    return render_template('user_table.html')

if __name__ == '__main__':
    app.run(debug=True)

