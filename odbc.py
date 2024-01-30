import psycopg2
from config import config


def connect(queryString : str):
    con = None

    try:
        params = config()

        print('Conectando a la BD POstgresql')
        #conn = psycopg2.connect(params)
        conn = psycopg2.connect(
            host="localhost",
            database="Usuarios",
            user="postgres",
            password="Kripton.postgres")
        

        #crea el cursor
        cur = conn.cursor()

        #executa la consulta
        print('ejecucion de consulta')
        cur.execute(queryString)


        rows = cur.fetchall()

        for row in rows:
            print(row)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print('conn no es null')
            print(conn)
            return conn,cur
            #conn.close()