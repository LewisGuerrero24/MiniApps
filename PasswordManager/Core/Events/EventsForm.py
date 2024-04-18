from Core.Scripts.ListSpaces import ListSpaces
from Components.Container import ComponentContainer
from Components.Cards import CardComponent
from Core.Data import Data


class EventsForm():
    def __init__(self,ft, page):
        self.ft = ft
        self.page = page
        
    def LisSpacesCard(self): 
        ArraySpaces = list()
        for i in ListSpaces():
            ArraySpaces.append(CardComponent(self.page,f"/List/Password/{i}","Go in",i,""))
        return ArraySpaces
    
    def ListPasswordCard(self,nameSpace,button_Copy_p,button_delete_p): 
        newData = Data(nameSpace)
        newData.load_Data()
        ArrayPassword = list()
        InitialOption = self.ft.dropdown.Option("Seleccione...")
        ArrayPassword.append(InitialOption)
        for i in newData.listDataByItem():
            NewOption = self.ft.dropdown.Option(i)
            ArrayPassword.append(NewOption)
            
        dd = self.ft.Dropdown(value="Seleccione...",width = 200,options = ArrayPassword)
        b = self.ft.ElevatedButton(text="Copy", on_click=lambda _: button_Copy_p(_,newData,dd))
        e = self.ft.ElevatedButton(text="Delete", on_click=lambda _: button_delete_p(_,newData,dd, nameSpace))
        
        PasswordCard = ComponentContainer(nameSpace,dd,b,e)
        return PasswordCard