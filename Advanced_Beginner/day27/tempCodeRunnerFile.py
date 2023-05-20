from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
my_label = Label(text="This is old text")
my_label.config(text="This is new text")
my_label.grid(column=0, row=0)
