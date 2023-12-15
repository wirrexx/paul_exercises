import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

window = tk.Tk()
window.title('Christmas Wishes')
window.geometry('340x440')
window.configure(bg='#333333')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

def load_imagE():
    
    file_path = filedialog.askopenfile()
    if file_path():
        image = Image.open(file_path)
        image = image.resize((400,400))
        photo = ImageTk.PhotoImage(image)
        # image_label.config(image=photo)
        # image_label.image = photo

def add_wish():
    wish = textbox.get()
    if wish:
        listbox.insert(tk.END, wish)
        textbox.delete(0, tk.END)
        wish = '\n' + wish
        save_wishes(wish)

def open_wishes():
    try:
        with open ('wishes.txt', 'r') as file:
            wishes = file.readlines()
            for wish in wishes:
                listbox.insert(tk.END, wish)
    except (FileNotFoundError):
        print('file not found')       
    except (Exception):
        print('File is missing or corrupt.')


def save_wishes(wish):
    try:
        with open ('wishes.txt', 'ab') as file:
            file.writelines(wish)
    except (FileNotFoundError):
        print('file not found')       
    except (Exception):
        print('File is missing or corrupt.')
        
label = tk.Label(window, text='Enter your christmas wish: ', background='#333333', foreground='white')
label.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')


textbox =tk.Entry(window, background='grey', foreground='white')
textbox.grid(row=1, column=0,columnspan=2, padx=10,pady=5,sticky='nsew', ipadx=3)

listbox = tk.Listbox(window, background='grey', foreground='white')
listbox.grid(row=2, column=0, columnspan=2, padx=10,pady=5, sticky='nsew')

# add wishes
add_button = tk.Button(window, text='Add', command=add_wish)
add_button.grid(row=3, column=0, columnspan=2,padx=10,pady=5,sticky='ew')

# open wishes
open_button= tk.Button(window, text='Load wishes', command=open_wishes)
open_button.grid(row=4, column=0,columnspan=2,padx=10,pady=5,sticky='ew') 


open_wishes()


window.mainloop()