import tkinter as tk

window = tk.Tk()
window.title('Christmas Wishes')
window.geometry('340x440')
window.configure(bg='#333333')


def add_wish():
    wish = textbox.get()
    if wish:
        listbox.insert(tk.END, wish)
        textbox.delete(0, tk.END)

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


def save_wishes():
    try:
        with open ('wishes.txt', 'a+') as file:
            wishes = file.readlines()
            for wish in wishes:
                listbox.insert(tk.END, wish)
    except (FileNotFoundError):
        print('file not found')       
    except (Exception):
        print('File is missing or corrupt.')
        
label = tk.Label(window, text='Enter your christmas wish: ', background='grey', foreground='white', pady=5)
label.pack()


textbox =tk.Entry(background='grey', foreground='white')
textbox.pack(pady=5)


listbox = tk.Listbox(window, width=20, height=5, background='grey', foreground='white')
listbox.pack(pady=5)

# add wishes
add_button = tk.Button(window, text='Add', command=add_wish)
add_button.pack(pady=2)

# open wishes
open_button= tk.Button(window, text='Open file', command=open_wishes)
open_button.pack(pady=2)



window.mainloop()