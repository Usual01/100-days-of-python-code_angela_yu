from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '.', '-', '_', '@', '#', '$', '%', '&', '*']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)

    password_str = "".join(password_list)
    
    password_entry.insert(0, password_str)


def save():

    website = Website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
        "email": email,
        "password": password,
        }
    }
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(message="more words pls")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
             with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            

             
        finally:
            Website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = Website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPasword: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exists!")


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

Website_entry = Entry(width=21)
Website_entry.grid(row=1, column=1)
Website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "MIKEDAMI@GMAIL.COM")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)

generate_p_b = Button(text="generate Password", command=generate_password)
generate_p_b.grid(row=3, column=2)
add_button = Button(text='Add', width = 35, command = save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()