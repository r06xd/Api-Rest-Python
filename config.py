from configparser import ConfigParser

def config(filename='database.ini',section='postgresql'):
    #crea el parser
    parser = ConfigParser()

    #lee el arhivo de configuracion
    parser.read(filename)

    #obtiene la section default a postgresql
    db={}
    if(parser.has_section(section)):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Selection {0} not fund in the {1}'.format(section,filename))
    
    return db