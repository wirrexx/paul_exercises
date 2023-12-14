import tkinter as tk
​
​
def change_text():
    display.config(text=textbox.get(), foreground="Red", background="Green")
​
​
window = tk.Tk()
window.geometry("300x200")
window.title("Christmas app")
label = tk.Label(text="Your wish will come true if you type it:", pady=5)
label.pack()
textbox = tk.Entry()
textbox.pack(ipadx=5, ipady=5)
display = tk.Label(padx=10, pady=20)
display.pack()
button = tk.Button(text="Add wish", command=change_text)
button.pack()
​
# Try adding wishes to a listbox
​
# Explore all properties of label, entry, button
​
# Explore other GUI elements
​
# Try to create an email screen
​