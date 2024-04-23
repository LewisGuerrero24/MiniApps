from Components.Container import ComponentContainer
from Components.Cards import CardComponent
from Core.Data import Data
from Core.Spaces import space


class EventsForm():
    def __init__(self,ft, page):
        self.ft = ft
        self.page = page     
  
    def LisSpacesCard(self,on_column_scroll): 
        newSpace = space()
    
        cl = self.ft.Column(
        spacing=10,
        height=350,
        width=420,
        scroll=self.ft.ScrollMode.ALWAYS,
        on_scroll=on_column_scroll,
    )   
        if len(newSpace.ListSpaces()) !=  0:
            for i in newSpace.ListSpaces():
                cl.controls.append(CardComponent(self.page,f"/List/Password/{i}","Go in",i,""))
            return cl
        else:
            textInformation = self.ft.Column([self.ft.Text("There are no spaces available...", size=25, color="pink600", italic=True),
                                              self.ft.ElevatedButton("Volver",on_click = lambda _: self.page.go("/"),icon="arrow_back_ios")])
            return textInformation
    
    def ListPasswordCard(self,nameSpace,button_Copy_p,button_delete_p): 
        newData = Data(nameSpace)
        newData.load_Data()
        ArrayPassword = list()
        InitialOption = self.ft.dropdown.Option("Seleccione...")
        ArrayPassword.append(InitialOption)
        for i in newData.listDataByItem():
            NewOption = self.ft.dropdown.Option(i)
            ArrayPassword.append(NewOption)
        DropPassword = self.ft.Dropdown(value="Seleccione...",width = 200,options = ArrayPassword)
        PasswordCard = ComponentContainer(nameSpace,self.page,DropPassword,lambda _: button_Copy_p(_,newData,DropPassword),lambda _: button_delete_p(_,nameSpace,newData,DropPassword))
        return PasswordCard
    
    