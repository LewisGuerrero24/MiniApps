import flet as ft

def ButtonsListPassword(Name,event,icon):
     btn = ft.ElevatedButton(text=Name, on_click=event, icon = icon)
     return btn