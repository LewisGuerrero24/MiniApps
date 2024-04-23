import pickle
from Core.EncryptData import Encrypt, DeEncrypt


class Data():  
    def __init__(self, nameSpace):
        self.nameSpace = nameSpace
        self.datos_recuperados = None
        self.route = f"./SpacesUser/{self.nameSpace}"
        
    #Insertar Nuevos Datos
    def newData(self,NameItem, Password):  
        DataEncrypt =Encrypt(Password)
        NewData =  {"Item": NameItem.upper().strip(),"Password":DataEncrypt[0],"Key":DataEncrypt[1]}
        if self.datos_recuperados is None:
                self.datos_recuperados = list()
                self.datos_recuperados.append(NewData)
        else: 
            if self.ExistItemData(NameItem.upper()) != True:
                    self.datos_recuperados.append(NewData)
        if self.Save_Data():
            return "Datos Creados Satisfactoriamente" 
        return "Ese Nombre de Item Ya Existe"
    
    #Cargar Datos
    def load_Data(self):
        with open(self.route, "rb") as archivo_binario:
            datos_recuperados = pickle.load(archivo_binario)
        self.datos_recuperados = datos_recuperados

    #Guardado de datos
    def Save_Data(self):
        with open(self.route, "wb") as archivo_binario:
            pickle.dump(self.datos_recuperados, archivo_binario)
        return True
        

    #Listar Usuarios   
    def listDataByItem(self):
        Items = list()
        for valor in self.datos_recuperados:
            Items.append(valor['Item'])
        return Items
    
    #devolver contraseña
    def passwordByPage(self,nameItem):
        for valor in self.datos_recuperados:
            if str(valor['Item']) == nameItem:
                return DeEncrypt(valor['Key'],valor['Password'])
        return "Data No encontrada"
    
    #Eliminar Data
    def deleteData(self,nameItem):
        for objeto in self.datos_recuperados:
            if objeto["Item"] == nameItem.upper():
                self.datos_recuperados.remove(objeto)
                if self.Save_Data():
                    return "Datos eLIMINADOS Satisfactoriamente"
                
    #Verificar si un Item ya existe    
    def ExistItemData(self,nameItem):
        for data in self.datos_recuperados:
            if data["Item"] == nameItem:
                return True
