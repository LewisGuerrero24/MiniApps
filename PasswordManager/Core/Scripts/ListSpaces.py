import os


def ListSpaces():
    carpeta = './SpacesUser/'
    archivos = os.listdir(carpeta)
    return archivos


