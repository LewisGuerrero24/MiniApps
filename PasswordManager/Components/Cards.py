import flet as ft



def CardComponent(page,Route,NameButton, NameTittle, NameSubtitle):
    Card = ft.Card(  )
    Card.content = ft.Container( ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.SPACE_DASHBOARD_ROUNDED),
                                title=ft.Text(NameTittle),
                                subtitle=ft.Text(
                                    NameSubtitle
                                ),
                            ),
                            ft.Row(
                                [ft.TextButton(NameButton,on_click=lambda _: page.go(Route))],
                                alignment=ft.MainAxisAlignment.END,
                            )
                        ]
                    ),
                width=400,
                padding=10,                   
                )
    return Card