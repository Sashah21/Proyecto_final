from datetime import datetime, date
import re, hashlib, os

def formato_fecha(fecha:str) -> int|None:
    #https://docs.python.org/3/library/datetime.html
    try:
        formato = '%Y-%m-%d'
        fecha_date = datetime.strptime(fecha,formato).date()
        hoy = date.today()
        edad = hoy.year - fecha_date.year
        #Si el dia es anterior a su cumple, se le restara uno.
        if (hoy.month,hoy.day) < (fecha_date.month,fecha_date.day):
            edad -= 1
        return edad
    except ValueError:
        return None
    
def confirmar_usuario(usuario:dict,reescribir:bool = False):
    '''Lanzara un ValueError en caso de error'''
    #devuelve la edad en vez de su fecha de nacimiento
    if not reescribir:
        if formato_fecha(usuario['edad']):
            usuario['edad'] = formato_fecha(usuario['edad'])
        else:
            raise ValueError
    #RegEx
    re_nombre = r'[a-zA-z]{3,12}'
    re_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    re_password = r'.{8,}'
    re_tfno = r'[0-9]{9}'
    #Comprobacion de RegEx
    if     not re.match(re_nombre,usuario['nombre']) \
        or not re.match(re_nombre,usuario['apellidos']) \
        or not re.match(re_email,usuario['email']) \
        or not re.match(re_password,usuario['contraseña']) \
        or not re.match(re_tfno,str(usuario['telefono'])):
        raise ValueError
    else:
        usuario['contraseña'] = encriptar_contraseña(usuario['contraseña'])
        return 
    
def encriptar_contraseña(contraseña:str):
    sal = os.urandom(32) #Secuencia de bytes aleatorios
    encriptado = hashlib.pbkdf2_hmac('sha256',contraseña.encode('utf-8'),sal,50)
    return [encriptado.hex(),sal.hex()]

def confirmar_contraseña(lista_pass:list,input:str) -> bool:
    sal = bytes.fromhex(lista_pass[1]) #Lo convertimos de vuelta a byte
    contraseña_original = lista_pass[0]
    contraseña_input = hashlib.pbkdf2_hmac('sha256',input.encode('utf-8'),sal,50).hex() #usa lo mismo para convertirla a hex
    return contraseña_input == contraseña_original #Compara los hex
