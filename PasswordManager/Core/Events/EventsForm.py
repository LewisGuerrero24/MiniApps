from Core.Scripts.ListSpaces import ListSpaces
from Components.Container import ComponentContainer
from Components.Cards import CardComponent
from Core.Data import Data


class EventsForm():
    def __init__(self,ft, page):
        self.ft = ft
        self.page = page     
  
    def LisSpacesCard(self,on_column_scroll): 
        cl = self.ft.Column(
        spacing=10,
        height=350,
        width=420,
        scroll=self.ft.ScrollMode.ALWAYS,
        on_scroll=on_column_scroll,
    )
        for i in ListSpaces():
            cl.controls.append(CardComponent(self.page,f"/List/Password/{i}","Go in",i,""))
        return cl
    
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
        b = self.ft.ElevatedButton(text="Copy", on_click=lambda _: button_Copy_p(_,newData,dd), icon = "content_copy")
        e = self.ft.ElevatedButton(text="Delete", on_click=lambda _: button_delete_p(_,newData,dd, nameSpace),icon  = "delete")
        lk = self.ft.ElevatedButton(text="Create",on_click=lambda _: self.page.go(f"/Create/Password/{nameSpace}"),icon  = "create")
        ng =self.ft.ElevatedButton("volver",icon = "arrow_back_ios",on_click=lambda _: self.page.go("/"))
        PasswordCard = ComponentContainer(nameSpace,dd,b,e,lk, ng)
        return PasswordCard
    
    