from tkinter import *

def m2k():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer.config(text=f"{km}")

window = Tk()
window.title("miles to kilometer converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column = 1, row = 0)

miles_label = Label(text="Miles")
miles_label.grid(column = 2, row = 0)

is_equal = Label(text="is equal")
is_equal.grid(column = 0, row = 1)

kilometer = Label(text="0")
kilometer.grid(column = 1, row = 1)

kilometer_label = Label(text="km")
kilometer_label.grid(column = 2, row = 1)

calc_button = Button(text="Calculate" , command=m2k)
calc_button.grid(column = 1, row = 2)

window.mainloop()