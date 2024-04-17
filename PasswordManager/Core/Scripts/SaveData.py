import os
import pickle


def Save_Data(datos_recuperados, nameSpace):
        nombre_archivo = f'./SpacesUser/{nameSpace}'
        with open(nombre_archivo, "wb") as archivo_binario:
            pickle.dump(datos_recuperados, archivo_binario)
        return True



