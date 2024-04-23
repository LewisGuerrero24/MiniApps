import pyperclip as clipboard
from Core.Data import Data
from Core.Spaces import space

class EventsOnclick():
    def __init__(self,page):
        self.page = page
        
    #Create Spaces en Python
    def CreateSpa(self,e, k):
        newSpace = space(k.value)
        print(newSpace.CreateSpace())
        self.page.go(f"/Create/Password/{k.value}")
        k.value = ""
        
        
    def CreatePassword(self,e,NameSpace,NameItem, Password):
        newData = Data(NameSpace) 
        newData.load_Data()
        print(newData.newData(NameItem.value, Password.value))
        self.page.go(f"/List/Password/{NameSpace}")
        
            
    # Lista de Passwords de un Usuario
    def button_Copy_p(self,e, newData,dd):
        print(dd.value)
        newData.load_Data() 
        clipboard.copy(newData.passwordByPage(dd.value))
        
    def button_delete_p(self,e,nameSpace,newData,dd):
        print(dd.value)
        print(newData.deleteData(dd.value)) 
        self.page.go(f"/List/Spaces")
