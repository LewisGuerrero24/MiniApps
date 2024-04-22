import os
def DeleteSpace(e,nameSpace):
    try:
        os.remove('./SpacesUser/{nameSpace}')
        print("Archivo eliminado correctamente.")
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as f:
        print("Ocurrió un error al intentar eliminar el archivo:", f)