import flet as ft
 


def main(page: ft.Page):

     page.window_width = 430.0
     page.window_height = 420.0
     
     page.on_resize

     def valores(e,numero):
         e.valor += numero
         print(str(e.valor))
         return e.valor
     
     def numero0(e):
         tb1.value += f"{0}"
         page.update()
         
     def numero1(e):
         tb1.value+= f"{1}"
         page.update()
     
     def numero2(e):
         tb1.value+= f"{2}"
         page.update()
             
     def numero3(e):
         tb1.value+= f"{3}"
         page.update()
         
     def numero4(e):
         tb1.value+= f"{4}"
         page.update()
         
     def numero5(e):
         tb1.value+= f"{5}"
         page.update()   
         
         
     def numero6(e):
         tb1.value+= f"{6}"
         page.update()
            
     def numero7(e):
         tb1.value+= f"{7}"
         page.update()
            
     def numero8(e):
         tb1.value+= f"{8}"
         page.update()
            
     def numero9(e):
         tb1.value+= f"{9}"
         page.update()  
         
     def sumar(e):
         tb1.value += "+" 
         page.update()
         
     def restar(e):
         tb1.value += "-" 
         page.update()   
     def mod(e):
         tb1.value +="%"
         page.update() 
         
     def multipli(e):
         tb1.value += "*" 
         page.update()
         
     def dividi(e):
         tb1.value += "/" 
         page.update()
         
     def ce(e):
         lista = [] 
         for i in tb1.value:
             lista.append(i)
         
         lista.pop()
         print(lista)
         tb1.value = ""
         for j in lista:
             tb1.value += j
         page.update() 
               
     def punto(e):
         tb1.value += "." 
         page.update()
              
         
     def igual(e):
         tb1.value = f"{eval(tb1.value)}"
         page.update()  
         
     def limpiar(e):
         tb1.value = ""
         page.update()
     tb1 = ft.TextField(width=400, bgcolor=ft.colors.BLUE_50, color="black",
                        text_align="RIGHT", disabled=True)
     
     btn0=ft.ElevatedButton(text="CE",bgcolor=ft.colors.INDIGO_100, color="black", width=90, on_click=ce)
     btn1=ft.ElevatedButton(text="Mod",bgcolor=ft.colors.INDIGO_100, color="black", width=90, on_click=mod)
     btn2=ft.ElevatedButton(text="AC",bgcolor=ft.colors.INDIGO_100, color="black", width=90, on_click=limpiar)
     btn3=ft.ElevatedButton(text="÷",bgcolor=ft.colors.ORANGE_300, color="black", width=90, on_click=dividi)
     
     btn4 = ft.ElevatedButton(text="7",bgcolor=ft.colors.INDIGO_100, color="black", width=90,on_click=numero7)
     btn5 = ft.ElevatedButton(text="8",bgcolor=ft.colors.INDIGO_100, color="black", width=90,on_click=numero8)
     btn6 = ft.ElevatedButton(text="9",bgcolor=ft.colors.INDIGO_100, color="black", width=90,on_click=numero9)
     btn7 =ft.ElevatedButton(text="x",bgcolor=ft.colors.ORANGE_300, color="black", width=90, on_click=multipli)
     btn8=ft.ElevatedButton(text="4",bgcolor=ft.colors.INDIGO_100, color="black", width=90,on_click=numero4)
     btn9=ft.ElevatedButton(text="5",bgcolor=ft.colors.INDIGO_100, color="black", width=90,on_click=numero5)
     btn10=ft.ElevatedButton(text="6",bgcolor=ft.colors.INDIGO_100, color="black", width=90,on_click=numero6)
     btn11=ft.ElevatedButton(text="-",bgcolor=ft.colors.ORANGE_300, color="black", width=90, on_click=restar)
     btn12=ft.ElevatedButton(text="1",bgcolor=ft.colors.INDIGO_100, color="black", width=90,on_click=numero1)
     btn13=ft.ElevatedButton(text="2",bgcolor=ft.colors.INDIGO_100, color="black", width=90,on_click=numero2)
     btn14=ft.ElevatedButton(text="3",bgcolor=ft.colors.INDIGO_100, color="black", width=90,on_click=numero3)
     btn15=ft.ElevatedButton(text="+",bgcolor=ft.colors.ORANGE_300, color="black", width=90,on_click=sumar)
     btn16=ft.ElevatedButton(text="0",bgcolor=ft.colors.INDIGO_100, color="black", width=190, on_click=numero0)
     btn17=ft.ElevatedButton(text=".",bgcolor=ft.colors.INDIGO_100, color="black", width=90,on_click=punto)
     btn18=ft.ElevatedButton(text="=",bgcolor=ft.colors.ORANGE_300, color="black", width=90, on_click=igual)
     
 
     Rowbtn = ft.Row([
         btn0,
         btn1,
         btn2,
         btn3, 
     ])
     
    
     Rowbtn1 = ft.Row([
         btn4,
         btn5,
         btn6,
         btn7,     
     ])
     
     Rowbtn2 = ft.Row([
         btn8,
         btn9,
         btn10,
         btn11,   
     ])
     
     Rowbtn3 = ft.Row([
         btn12,
         btn13,
         btn14,
         btn15
          
     ])
     
     Rowbtn4 = ft.Row([
         btn16,
         btn17,
         btn18,
          
     ])
     
     
     page.add(tb1, Rowbtn,Rowbtn1, Rowbtn2, Rowbtn3, Rowbtn4)
     
ft.app(target = main)