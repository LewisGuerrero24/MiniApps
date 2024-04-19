import flet as ft

def ComponentContainer(nameSpace,dd,b,e,lk,ng):
    Container = ft.Container(
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
                            ft.Row(
                                [lk,ng],
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