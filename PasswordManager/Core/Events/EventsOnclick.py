from Core.Scripts.CreateSpaces import CreateSpaces
from Core.Scripts.EliminateSpace import DeleteSpace
import pyperclip as clipboard
from Core.Data import Data

class EventsOnclick():
    def __init__(self, k):
        self.k = k
        
    #Create Spaces en Python
    def CreateSpa(self,e, page):
        print(CreateSpaces(self.k.value))
        page.go(f"/Create/Password/{self.k.value}")
        
        
    def CreatePassword(self,e,page,NameSpace,NamePassword, Password):
        newData = Data(NameSpace) 
        newData.load_Data()
        print(newData.newData(NamePassword.value, Password.value))
        page.go(f"/List/Password/{NameSpace}")
        
            
    # Lista de Passwords de un Usuario
    def button_Copy_p(self,e, newData,dd):
        print(dd.value)
        newData.load_Data() 
        clipboard.copy(newData.passwordByPage(dd.value))
        
    def button_delete_p(self,e, newData,dd):
        print(dd.value)
        print(newData.deleteData(dd.value)) 
