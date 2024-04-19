import flet as ft

def main(page: ft.Page):
    def on_column_scroll(e: ft.OnScrollEvent):
        print(
            f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
        )
        
        
        
    Card = ft.Card(  )
    Card.content = ft.Container(ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.SPACE_DASHBOARD_ROUNDED),
                                title=ft.Text("Card Neuevo Mundo"),
                                subtitle=ft.Text(
                                    "pequeño mundo"
                                ),
                            ),
                            ft.Row(
                                [ft.TextButton("hola mundo")],
                                alignment=ft.MainAxisAlignment.END,
                            )
                        ]
                    ),
                width=400,
                padding=10,              
                )
    cl = ft.Column(
        spacing=10,
        height=200,
        width=400,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll=on_column_scroll,
    )
    for i in range(0,10):
        cl.controls.append(Card)

    page.add(
        ft.Container(cl, border=ft.border.all(1)),
    )

ft.app(main)