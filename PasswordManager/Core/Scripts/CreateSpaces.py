import os
import pickle

def CreateSpaces(NameSpaces):
    ruta_archivo = f"./SpacesUser/{NameSpaces}"

    directorio = os.path.dirname(ruta_archivo)
    if not os.path.exists(directorio):
        os.makedirs(directorio)
        
    with open(ruta_archivo, "wb") as archivo_binario:
        pickle.dump(None, archivo_binario)

    print("Datos guardados correctamente en", ruta_archivo)
    
    
# NameSpaces = str(input("Ingrese el Nombre del espacio"))
# CreateSpaces(NameSpaces)



    
    
    