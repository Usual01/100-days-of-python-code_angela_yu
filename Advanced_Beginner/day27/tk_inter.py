import tkinter

window = tkinter.Tk()
window.title("my GUI")
window.minsize(width = 500, height = 300)

my_name = tkinter.Label(text='My name is damilola', font=("Arial", 30, "italic"))
my_name.pack()


window.mainloop()