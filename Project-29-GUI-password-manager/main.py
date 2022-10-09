from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 7)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbol + password_number + password_letter
    random.shuffle(password_list)

    password_gen = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, f"{password_gen}")
    pyperclip.copy(password_gen)


# ---------------------------- SEARCH ------------------------------- #
def search():
    with open("database.json", "r") as data_file:
        get_data = json.load(data_file)
        get_site_entry = site_entry.get()
        result = get_data[get_site_entry]
        pass_entry.delete(0, END)
        pass_entry.insert(0, result['password'])


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_detail():
    site = site_entry.get()
    password = pass_entry.get()
    email = email_entry.get()

    new_data = {
        site: {
            "email": email,
            "password": password,
        }
    }

    print(site, password, email)
    if len(site) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(
            title="Error", message="Make sure you have haven't left any fields empty.")
    else:
        is_ok = messagebox.askyesno(title="Details",
                                    message=f"These are the details entered \n \n \nEmail:{email}\nPassword:{password}\n"
                                            f"Website:{site}\n\nIs it ok to save ?\n")

        if is_ok:
            data = None
            with open("database.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

            with open("database.json", "w") as files:
                json.dump(data, files, indent=4)
                site_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_site = Label(text="Website :")
label_site.grid(column=0, row=1, sticky=W)
label_site.config(padx=5, pady=10)

site_entry = Entry(width=23, borderwidth=5, relief=FLAT)
site_entry.grid(column=1, row=1, sticky=W)

search_btn = Button(text="Search", width=13, command=search)
search_btn.grid(column=2, row=1, sticky=W)

label_email = Label(text="Email/Username :")
label_email.grid(column=0, row=2)
label_email.config(padx=5, pady=10)

email_entry = Entry(width=40, borderwidth=5, relief=FLAT)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "itsmedeepak@gmail.com")

label_pass = Label(text="Password :")
label_pass.grid(column=0, row=3)
label_pass.config(padx=0, pady=10)

pass_entry = Entry(width=23, borderwidth=5, relief=FLAT)
pass_entry.grid(column=1, row=3)

generate_btn = Button(text="Generate Password", width=16, command=pass_gen)
generate_btn.grid(column=2, row=3)
generate_btn.config(padx=0, pady=5)

add_btn = Button(text="Add", width=40)
add_btn.grid(column=1, row=4, columnspan=2)
add_btn.config(padx=5, pady=5, command=add_detail)

window.mainloop()
