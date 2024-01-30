import psycopg2
from config import config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask import Flask

def connect(name:str,queryString: str):

    resultado = None
    db = SQLAlchemy()
    app = Flask(name)
    try:

        print('Conectando a la BD POstgresql')
        print(app)
        #conn = psycopg2.connect(params)
        
        nombre_usuario = 'postgres'
        contrasenia = 'Kripton.postgres'
        nombre_servidor = 'localhost'
        nombre_bd = 'Usuarios'
        puerto = '5432'

        #conexion string
        conection_str = f'postgresql://{nombre_usuario}:{contrasenia}@{nombre_servidor}:{puerto}/{nombre_bd}'
        app.config['SQLALCHEMY_DATABASE_URI'] = conection_str
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        sql_query = text(queryString)
        db.init_app(app)
        with app.app_context():
            resultado = db.session.execute(sql_query)
            db.session.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if resultado is not None:
            return resultado
            #conn.close()