""" my_string = "Hello Coder! You have done it! "

iterator = iter(my_string)


while True: 

    item = next(iterator, 'end')
    if item == 'end':
        break
    print(item) """


import flet as ft 

def main(page: ft.page):
    # Använda koma tecken visar vad för parameter en funktion tar in
    page.window_width=500
    page.window_height=700
    page.bgcolor="#45898"

    
    textField = ft.TextField(width=400, height=50)
    addBtn = ft.ElevatedButton(text='Search')
    entries_row=ft.Row(controls=[textField, addBtn]) # måste komma på slutet av koden

    page.add(entries_row)




ft.app(target=main)