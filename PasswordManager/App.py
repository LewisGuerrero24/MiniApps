import flet as ft
from Components.Cards import CardComponent
from Core.EventsForm import EventsForm
from Core.EventsOnclick import EventsOnclick

def main(page):
     page.window_width = 430.0
     page.window_height = 420.0
     
     def on_column_scroll(e: ft.OnScrollEvent):
        print(
            f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
        )
    
    
     k = ft.TextField(label="Name Space");
     
     #Eventos de vistas y Clicks  
     Events = EventsForm(ft,page)
     EventsButtonOnclick = EventsOnclick(page)
    
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
        troute = ft.TemplateRoute(page.route)     
        if page.route == "/Create/Space":
            page.views.append(
                ft.View(
                    "/Space",
                    [
                        k,
                        ft.Row([ft.ElevatedButton("Crear",on_click=lambda _:EventsButtonOnclick.CreateSpa(_,k)),
                        ft.ElevatedButton("volver",icon = "arrow_back_ios",on_click=lambda _: page.go("/"))]),
                    ],
                )
            )
            

        if page.route == "/List/Spaces":
                
                page.views.append(
                    ft.View(
                        "/List",
                        
                            [Events.LisSpacesCard(on_column_scroll)],
                    )
                )
        
          
        if troute.match("/List/Password/:Name"): 
            if page.route == f"/List/Password/{troute.Name}":
                print("El espacio es de= " + troute.Name) 
                page.views.append(
                    ft.View(
                        f"/List/Password/{troute.Name}",
                            [Events.ListPasswordCard(troute.Name, EventsButtonOnclick.button_Copy_p, EventsButtonOnclick.button_delete_p),],
                    )
                )
                
        if troute.match("/Create/Password/:Name"):               
            if page.route == f"/Create/Password/{troute.Name}":
                    NameItem = ft.TextField(label="Name")
                    Password = ft.TextField(label="Password", password=True, can_reveal_password=True)
                    page.views.append(
                        ft.View(
                            f"/Create/Password/{troute.Name}",
                                [ft.Container(
                                    content=ft.Column(
                            [
                                ft.Row( [NameItem],
                                    alignment=ft.MainAxisAlignment.CENTER,   
                                ),
                                ft.Row(
                                    [Password,],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),   
                                ft.Row(
                                    [ft.ElevatedButton(text="Crear", on_click = lambda _:EventsButtonOnclick.CreatePassword(_,troute.Name,NameItem,Password)),
                                     ft.ElevatedButton("volver",icon = "arrow_back_ios",on_click=lambda _: page.go("/"))],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                )   
                            ]
                        ),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.BLACK12,
                        width=400,
                        height=300,
                        border_radius=10,
                    ),],
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