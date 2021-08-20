import tkinter
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_get = web_entry.get()
    email_get = email_entry.get()
    password_get = password_entry.get()

    if len(website_get) == 0 or len(password_get) == 0:
        messagebox.showinfo(title='Empty entry', message='the entries cannot be empty')

    else:
        is_ok = messagebox.askokcancel(title=website_get, message=f'Do you want to save these infos:'
                                                                  f'\nEmail/User: {email_get}\nPassword: {password_get}'
                                                                  f'\nFor {website_get} website ?')

        if is_ok:
            f = open('pass_project', 'a')
            f.write(f'{website_get} | {email_get} | {password_get}\n')
            web_entry.delete(0, 'end') # deleta do entry do programa o nome do site
            password_entry.delete(0, 'end') # deleta do entry do programa a senha
            f.close()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
padlock_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# WEBSITE LABEL
web_label = tkinter.Label(text='Website: ')
web_label.grid(column=0, row=1)

# WEBSITE ENTRY
web_entry = tkinter.Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky='EW')
web_entry.focus()

# EMAIL LABEL
email_label = tkinter.Label(text='Email/Username: ')
email_label.grid(column=0, row=2)

# EMAIL ENTRY
email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky='EW')
email_entry.insert(0, 'danilo@gmail.com')

# PASSWORD LABEL
password_label = tkinter.Label(text='Password: ')
password_label.grid(column=0, row=3)

# PASSWORD ENTRY
password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3, sticky='EW')

# PASSWORD BUTTON
password_button = tkinter.Button(text='Generate Password', command=generate_password)
password_button.grid(column=2, row=3)

# ADD BUTTON
add_button = tkinter.Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
