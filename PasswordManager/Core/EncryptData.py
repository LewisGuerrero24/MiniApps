import pickle
from cryptography.fernet import Fernet

def Encrypt(Password):
    clave = Fernet.generate_key()
    fernet = Fernet(clave)
    hash_password= fernet.encrypt(Password.encode())
    return [hash_password,clave]

def DeEncrypt(clave, password):
    fernet = Fernet(clave)
    datos_desencriptados = fernet.decrypt(password)
    datos_desencriptados = datos_desencriptados.decode('utf-8')
    return datos_desencriptados
    