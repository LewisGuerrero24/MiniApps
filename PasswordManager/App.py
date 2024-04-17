import flet as ft
import re
import repath
import pyperclip as clipboard
from Core.Scripts.ListSpaces import ListSpaces
from Core.Data import Data

def main(page):
    CreateCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.SPACE_DASHBOARD_ROUNDED),
                            title=ft.Text("Create new Spaces de Password"),
                            subtitle=ft.Text(
                                "Create a SPaces for you password."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Create",on_click=lambda _: page.go("/"))],
                            alignment=ft.MainAxisAlignment.END,
                        )
                    ]
                ),
                width=400,
                padding=10,
            )   
        )
    
    ListCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.SPACE_DASHBOARD_ROUNDED),
                            title=ft.Text("Acces Your Spaces"),
                            subtitle=ft.Text(
                                "Access the available spaces ."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("View",on_click=lambda _: page.go("/List/Spaces"))],
                            alignment=ft.MainAxisAlignment.END,
                        )
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    
    page.title = "Routes Example"
    
    # listar espacios creados por el usuario
    def LisSpacesCard(): 
        ArraySpaces = list()
        for i in ListSpaces():
            NewSpaceCard = ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.SPACE_DASHBOARD_ROUNDED),
                                title=ft.Text(i),
                            ),
                            ft.Row(
                                [ft.TextButton("Go in", on_click=lambda _: page.go(f"/List/Password/{i}"))],
                                alignment=ft.MainAxisAlignment.END,
                            )
                        ]
                    ),
                    width=400,
                    padding=10,
                )
            )
            ArraySpaces.append(NewSpaceCard)
        return ArraySpaces
    
    
    # Lista de Passwords de un Usuario
    def button_Copy_p(e, newData,dd):
        print(dd.value)
        newData.load_Data() 
        clipboard.copy(newData.passwordByPage(dd.value))
        
    def button_delete_p(e, newData,dd, nameSpace):
        print(dd.value)
        print(newData.deleteData(dd.value)) 
        page.go(f"/List/Password/{nameSpace}")
    
    
    def ListPasswordCard(nameSpace): 
        newData = Data(nameSpace)
        newData.load_Data()
        ArrayPassword = list()
        InitialOption = ft.dropdown.Option("Seleccione...")
        ArrayPassword.append(InitialOption)
        for i in newData.listDataByItem():
            NewOption = ft.dropdown.Option(i)
            ArrayPassword.append(NewOption)
            
        dd = ft.Dropdown(value="Seleccione...",width = 200,options = ArrayPassword)
        b = ft.ElevatedButton(text="Copy", on_click=lambda _: button_Copy_p(_,newData,dd))
        e = ft.ElevatedButton(text="Delete", on_click=lambda _: button_delete_p(_,newData,dd, nameSpace))
        
        PasswordCard = ft.Container(
                    content=ft.Column(
                        [
                            ft.Row( [ft.Text(nameSpace)],
                                alignment=ft.MainAxisAlignment.CENTER,   
                            ),
                            ft.Row(
                                [dd,],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),   
                            ft.Row(
                                [b,e],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),   
                        ]
                    ),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLACK12,
                    width=220,
                    height=200,
                    border_radius=10,
                )
        return PasswordCard

   
    
#   Rutas de las Vistas
    def route_change(route):       
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    CreateCard,
                    ListCard,
                ],
            )
        )
    
        if page.route == "/Create/Space":
            page.views.append(
                ft.View(
                    "/Space",
                    [
                        ft.TextField(label="Name Space"),
                        ft.ElevatedButton("Crear", on_click=lambda _: page.go("/")),
                    ],
                )
            )
            

        if page.route == "/List/Spaces":
                page.views.append(
                    ft.View(
                        "/List",
                            LisSpacesCard(),
                    )
                )
        
        troute = ft.TemplateRoute(page.route)   
        if troute.match("/List/Password/:Name"): 
            if page.route == f"/List/Password/{troute.Name}":
                print("El espacio es de= " + troute.Name) 
                page.views.append(
                    ft.View(
                        f"/List/Password/{troute.Name}",
                            [ListPasswordCard(troute.Name),],
                    )
                )
            
        # if page.route == "/List/Password":
        #     page.views.append(
        #         ft.View(
        #             "/List",
        #             [
        #                 LisSpacesCard,
        #             ],
        #         )
        #     )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)