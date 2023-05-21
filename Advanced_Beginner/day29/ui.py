from tkinter import *
from tkinter import messagebox

def save():

    website = Website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are ypur details:"
                           f"\nEmail{email} \npassword: {password}\nIs it ok to save?")
    if is_ok:

        with open("data.txt", "a") as data_file:
            data_file.write(f"The website is : {website} | The email is: {email} | and the password is: {password}\n")
            Website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("pomodoro")
window.config(padx= 20, pady=20, bg="yellow")

canvas = Canvas(width=200, height=200, bg="yellow", highlightthickness=0)
tomato_img = PhotoImage(file="fresher.gif")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(row=0, column=1)

Website_label = Label(text="website")
Website_label.grid(row=1, column=0)

email_label = Label(text="Email/username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

Website_entry = Entry(width=35)
Website_entry.grid(row=1, column=1 , columnspan=2)
Website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "MIKEDAMI@GMAIL.COM")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_p_b = Button(text="generate Password")
generate_p_b.grid(row=3, column=2)
add_button = Button(text='Add', width = 35, command = save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()