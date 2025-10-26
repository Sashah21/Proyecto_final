import json,methods
ruta = r'src\users.json'
#Create
def guardar_usuario_nuevo(usuario:dict):
    '''Carga los usuarios, añade el creado a la lista y lo guarda'''
    json_users:list = cargar_lista_usuarios()
    if len(json_users) > 0:
        new_id:int = json_users[-1]['id'] + 1
    else:
        new_id:int = 1
    usuario['id'] = new_id
    json_users.append(usuario)
    reescribir_datos(json_users)
#Read
def obtener_usuario(user_id:int) -> dict|None:
    '''Obtiene un usuario en concreto de la lista'''
    lista:list = cargar_lista_usuarios()
    for usuario in lista:
        if usuario['id'] == user_id:
            return usuario
    return None

def cargar_lista_usuarios() -> list|None:
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
#Update
def modificar_usuario(usuario_editado:dict):
    '''Edita el usuario con la informacion introducida, devuelve un booleano si lo ha editado o no'''
    lista = cargar_lista_usuarios()
    for index,usuario in enumerate(lista):
        if usuario['id'] == usuario_editado['id']:
            lista[index] = usuario_editado
            reescribir_datos(lista)
            return True
    return False

def reescribir_datos(lista:list):
    '''Reescribe la informacion del archivo json con la informacion introducida'''
    global ruta
    try:
        with open(ruta,'w') as archivo:
            json.dump(lista,archivo,indent=4)
    except json.JSONDecodeError as e:
        print(f'\nerror en la decodificacion. \n{e}\n')
    except FileNotFoundError as e:
        print(f'\nArchivo no encontrado. \n{e}\n')
#Delete
def eliminar_usuario(user_id:int):
    '''Elimina un usuario concreto de la lista, devuelve un booleano si lo encuentra o no.'''
    lista:list = cargar_lista_usuarios()
    for idx,usuario in enumerate(lista):
        if usuario['id'] == user_id:
            lista.pop(idx)
            reescribir_datos(lista)
            return True
    return False