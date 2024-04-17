import pickle
from Core.Scripts.EncryptData import Encrypt, DeEncrypt
from Core.Scripts.SaveData import Save_Data
from Core.Scripts.ExistData import ExistItemData

class Data():  
    def __init__(self, nameSpace):
        self.nameSpace = nameSpace
        self.datos_recuperados = None
    
    def newData(self,NameItem, Password):  
        DataEncrypt =Encrypt(Password)
        NewData =  {"Item": NameItem.upper().strip(),"Password":DataEncrypt[0],"Key":DataEncrypt[1]}
        
        if ExistItemData(NameItem.upper(),self.datos_recuperados) != True:
            if self.datos_recuperados is None:
                self.datos_recuperados = [NewData]
            else: 
                self.datos_recuperados.append(NewData)
            if Save_Data(self.datos_recuperados, self.nameSpace):
                return "Datos Creados Satisfactoriamente"
            
            return "Datos no se han Podido Cargar Correctamente"
        return "Ese Nombre de Item Ya Existe"
        
        
    def load_Data(self):
        nombre_archivo = f'./SpacesUser/{self.nameSpace}'
        with open(nombre_archivo, "rb") as archivo_binario:
            datos_recuperados = pickle.load(archivo_binario)
        self.datos_recuperados = datos_recuperados

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
    
    def deleteData(self,nameItem):
        for objeto in self.datos_recuperados:
            if objeto["Item"] == nameItem.upper():
                self.datos_recuperados.remove(objeto)
                if Save_Data(self.datos_recuperados, self.nameSpace):
                    return "Datos eLIMINADOS Satisfactoriamente"
        
            
lt = Data('lewis')
lt.load_Data()
# lt.deleteData('messenger')
print(lt.newData("messenger","aramis2409"))
lt.load_Data()
