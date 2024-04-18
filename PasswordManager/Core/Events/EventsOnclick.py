from Core.Scripts.CreateSpaces import CreateSpaces
import pyperclip as clipboard

class EventsOnclick():
    def __init__(self, k):
        self.k = k
        
    #Create Spaces en Python
    def CreateSpa(self,e):
        print(CreateSpaces(self.k.value))
    
    # Lista de Passwords de un Usuario
    def button_Copy_p(self,e, newData,dd):
        print(dd.value)
        newData.load_Data() 
        clipboard.copy(newData.passwordByPage(dd.value))
        
    def button_delete_p(self,e, newData,dd):
        print(dd.value)
        print(newData.deleteData(dd.value)) 
