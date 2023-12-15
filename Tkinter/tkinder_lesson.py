import tkinter as tk

window = tk.Tk()
window.title('My sec app')
window.geometry('600x400')

label = tk.Label(text ='Please enter your wish:', padx=10, pady=10) # function
label.pack() # kallar på funktion
textbox = tk.Entry(background='black', foreground='yellow') # knapp function
textbox.pack(ipady=5, ipadx=20)  # kallar på funktion
button = tk.Button(text='click me', padx=20, pady=0) # funktion knapp
button.pack() # kallar på knappen
listBox = tk.Listbox()
listBox.pack()

window.mainloop()