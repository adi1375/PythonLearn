from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

letters_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols_list = ["!", "#", "$", "%", "(", ")", "*", "+"]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0,END)
    letters = randint(8, 10)
    numbers = randint(2,4)
    symbols = randint(2,4)
    
    password_list = [choice(letters_list) for _ in range(letters)]
    password_list += [choice(numbers_list) for _ in range(numbers)]
    password_list += [choice(symbols_list) for _ in range(symbols)]
    
    # for i in range(letters):
    #     password_list += random.choice(letters_list)
    # for i in range(numbers):
    #     password_list += random.choice(numbers_list)
    # for i in range(symbols):
    #     password_list += random.choice(symbols_list)

    shuffle(password_list)
    password = "".join(password_list)
    
    entry_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="Empty Data Fields!\nPlease fill the necessary fields.")
    else:    
        is_ok =messagebox.askokcancel(title=f"{website}",message=f"These are the details entered: \nEmail: {email} \nPassword: {password} Is it ok to save?")
    
        if is_ok:
            with open("Python_100_days/Day_29_Password_Manager/password.txt",mode="a") as file:
               file.write(f"{website} | {email} | {password}\n")
               entry_website.delete(0,END)
               entry_email.delete(0,END)
               entry_password.delete(0,END)
               entry_website.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MY PASSWORD MANAGER")
window.config(padx=50,pady=50)

# image
canvas = Canvas(width=200,height=200)
lock = PhotoImage(file="Python_100_days/Day_29_Password_Manager/logo.png")
canvas.create_image(100,100, image=lock)
canvas.grid(row=0,column=1)

# Website row
label_website = Label(text="Website:")
label_website.grid(row=1,column=0)

entry_website = Entry(width=52)
entry_website.focus()
entry_website.grid(row=1,column=1,columnspan=2)

# Email row
label_email = Label(text="Email/Username:")
label_email.grid(row=2,column=0)

entry_email = Entry(width=52)
entry_email.insert(0,"abc@example.com")
entry_email.grid(row=2,column=1,columnspan=2)

# Password row
label_password = Label(text="Password:")
label_password.grid(row=3,column=0)

entry_password = Entry(width=34)
entry_password.grid(row=3,column=1)

button_password = Button(text="Generate Password", width= 14,command=generate_password)
button_password.grid(row=3,column=2)

# Button Add
button_add = Button(text="Add", width=44,command=save_data)
button_add.grid(row=4,column=1,columnspan=2)

window.mainloop()