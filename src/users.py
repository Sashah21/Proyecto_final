import json
ruta = r'src\users.json'
def cargar_lista_usuarios() -> dict|None:
    '''Accede a los usuarios a traves del index \n\n Ejemplo: usuarios[0]['email']'''
    global ruta
    usuarios = None
    try:
        with open(ruta,'r') as archivo:
            usuarios = json.load(archivo)
    except json.JSONDecodeError as e:
        print(f'\nerror en la decodificacion. \n{e}\n')
        pass
    except FileNotFoundError as e:
        print(f'\nArchivo no encontrado. \n{e}\n')
    return usuarios

def guardar_usuario(usuario:dict):
    '''Carga los usuarios, añade el creado a la lista y lo guarda'''
    json_users:list = cargar_lista_usuarios()
    if len(json_users) > 0:
        new_id:int = json_users[-1]['id'] + 1
    else:
        new_id:int = 1
    usuario['id'] = new_id
    json_users.append(usuario)
    global ruta
    try:
        with open(ruta,'w') as archivo:
            json.dump(json_users,archivo,indent=4)
    except json.JSONDecodeError as e:
        print(f'\nerror en la decodificacion. \n{e}\n')
    except FileNotFoundError as e:
        print(f'\nArchivo no encontrado. \n{e}\n')