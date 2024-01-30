from flask import Flask, jsonify,request
from odbc import connect
from conexionbd import connect

from flask_restx import Api,Resource, fields

app = Flask(__name__)
conn = None

api = Api(app,version='1.0',title='Api Rest con flask y postgres', description='Api basico que consume SP desde postgres')

nd = api.namespace('usuarios', description='Operaciones relacionadas con usuarios')

modelo_api_insertar = api.model('InsertarUsuario',{
    'nombre':fields.String(required=True,description='Nombre del usuario'),
    'direccion':fields.String(equired=True,description='direccion del usuario'),
    'telefono':fields.Integer(equired=True,description='telefono del usuario')
})

@nd.route('/')
class Usuarios(Resource):
    def get(self):
        conn = connect(__name__,'select * from consultar()')
        
        usuarios = [dict(row._asdict()) for row in conn]

        return jsonify(usuarios)

@nd.route('/insertar')
class InsertarUsuario(Resource):
    @api.expect(modelo_api_insertar)
    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            nombre = json['nombre'] if 'nombre' in json else '' 
            direccion = json['direccion'] if 'direccion' in json else '' 
            telefono = json['telefono'] if 'telefono' in json else '' 

            strQuery = f'''
                    CALL public.insert_user(
                        '{nombre}', 
                        '{direccion}',
                        {telefono}
                    )
                '''
                
            conn = connect(__name__,strQuery)
            print('==> insertados')
            print(strQuery)
            return "recibido ok"
        
@app.route('/api/doc')
def swagger():
    return jsonify(api.__schema__)

if __name__ == '__main__':
    app.run(debug=True)
    conn[0].close()
    