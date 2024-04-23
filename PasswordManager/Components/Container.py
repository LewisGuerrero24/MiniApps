import flet as ft
from Components.ButtonsListPassword import ButtonsListPassword
from Core.Spaces import space
def ComponentContainer(nameSpace,page,dropPassword,functionCopy,functionDelete):
    newSpace = space(nameSpace)
    Container = ft.Container(
                    content=ft.Column(
                        [ft.Row( [ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(text="Delete Space",on_click=lambda _: newSpace.DeleteSpace(_,page)),
                                    ]
                                )],
                                alignment=ft.MainAxisAlignment.START,   
                            ),
                            ft.Row( [ft.Text(nameSpace)],
                                alignment=ft.MainAxisAlignment.CENTER,   
                            ),
                            ft.Row(
                                [dropPassword,],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),   
                            ft.Row(
                                [ButtonsListPassword("Copy",functionCopy,"content_copy"),
                                 ButtonsListPassword("Create",lambda _: page.go(f"/Create/Password/{nameSpace}"),"create")],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [ButtonsListPassword("Delete",functionDelete,"delete"),
                                 ButtonsListPassword("volver",lambda _: page.go("/"),"arrow_back_ios")],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),    
                        ]
                    ),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLACK12,
                    width=420,
                    height=350,
                    border_radius=10,
                )
    return Container


    