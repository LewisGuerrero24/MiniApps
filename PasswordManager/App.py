import flet as ft
import re
import repath
import pyperclip as clipboard
from Components.Cards import CardComponent
from Core.Events.EventsForm import EventsForm
from Core.Events.EventsOnclick import EventsOnclick
from Core.Scripts.CreateSpaces import CreateSpaces
from Core.Data import Data

def main(page):
    
    k = ft.TextField(label="Name Space");  
    Events = EventsForm(ft,page)
    EventsButtonOnclick = EventsOnclick(k)
    
    
    page.title = "Routes Example"
    
    
#   Rutas de las Vistas
    def route_change(route):       
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    CardComponent(page,"/Create/Space","Create","Create New Space", "Create New space of passwords" ),
                    CardComponent(page,"/List/Spaces","View","Acces Your Spaces","Access the available spaces ."),
                ],
            )
        )
    
        if page.route == "/Create/Space":
            page.views.append(
                ft.View(
                    "/Space",
                    [
                        k,
                        ft.ElevatedButton("Crear",on_click=EventsButtonOnclick.CreateSpa),
                    ],
                )
            )
            

        if page.route == "/List/Spaces":
                page.views.append(
                    ft.View(
                        "/List",
                            Events.LisSpacesCard(),
                    )
                )
        
        troute = ft.TemplateRoute(page.route)   
        if troute.match("/List/Password/:Name"): 
            if page.route == f"/List/Password/{troute.Name}":
                print("El espacio es de= " + troute.Name) 
                page.views.append(
                    ft.View(
                        f"/List/Password/{troute.Name}",
                            [Events.ListPasswordCard(troute.Name, EventsButtonOnclick.button_Copy_p, EventsButtonOnclick.button_delete_p),],
                    )
                )
                
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)