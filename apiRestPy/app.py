from flask import Flask

#TODO: Crear una instancia de la aplicacion Flask
app = Flask(__name__)

#TODO: Definir una ruta para la pagina principal
@app.route('/')
def hola_mundo():
    return 'Hola Mundo'

#TODO: Iniciar la aplicacion si este script es ejecutado directamente
if __name__ == '__main__':
    #TODO: Configuracion para ejecutar la aplicacion en modo depuracion
    app.run(debug=True)