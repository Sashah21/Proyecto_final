import json
class Usuario():
    def __init__(self,*args):
        datos = {}
        for idx,data in enumerate(datos):
            datos = args[idx]

def cargar_lista_usuarios():
    ruta = r'src\users.json'
    usuarios = "None"
    try:
        with open(ruta,'r') as archivo:
            usuarios = json.load(archivo)
    except json.JSONDecodeError as e:
        print(f'\nerror en la decodificacion. \n{e}\n')
        pass
    except FileNotFoundError as e:
        print(f'\nArchivo no encontrado. \n{e}\n')
    #Accede a los usuarios a traves del index
    #print(usuarios[1])
    #print(usuarios[0]['email'])
    return usuarios

