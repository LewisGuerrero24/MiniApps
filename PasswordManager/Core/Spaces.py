import os
import pickle

class space():
    def __init__ (self, nameSpace = None):
        if nameSpace is not None:
            self.nameSpace = nameSpace
            self.route = f"./SpacesUser/{self.nameSpace}"
        
    def ListSpaces(self):
        carpeta = './SpacesUser/'
        archivos = os.listdir(carpeta)
        return archivos    
            
    def CreateSpace(self):
        directorio = os.path.dirname(self.route)
        if not os.path.exists(directorio):
            os.makedirs(directorio)
            
        with open(self.route, "wb") as archivo_binario:
            pickle.dump(None, archivo_binario)
        print("Datos guardados correctamente en", self.route)
        
        
    def DeleteSpace(self,e,page):
        try:
            os.remove(self.route)
            print("Archivo eliminado correctamente.")
            page.go("/")
        except FileNotFoundError:
            print("El archivo no existe.")
        except Exception as f:
            print("Ocurrió un error al intentar eliminar el archivo:", f)

