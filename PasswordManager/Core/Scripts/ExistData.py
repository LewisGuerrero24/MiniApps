import os
import pickle

def ExistItemData(nameItem, datos_recuperados):
    for data in datos_recuperados:
        if data["Item"] == nameItem:
            return True
    