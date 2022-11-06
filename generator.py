# Python program to generate a random password using the Tkinter module
import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.font as tkFont
import Levenshtein
import os
import sys

# Open the password file to populate the password list field
file1 = open(os.path.join(sys.path[0], "test.txt"), "r")


# Function for calculation of password
def low():
    entry.delete(0, END)
 
    # Get the length of password
    length = var1.get()
 
    # Make sure to omit ":" to avoid conflict with the update_file function and "\" to avoid potential newlines
    lower = "abcdefghijklmnopqrstuvwxyz0123456789"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+/<>?,.;"
    password = ""
 
    # if strength selected is low
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
 
    # if strength selected is medium
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
 
    # if strength selected is strong
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")
 
 
# Function for generation of password
def generate():
    password1 = low()
    entry.insert(10, password1)
 
 
# Function for copying password to clipboard
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)
    
def yes_button():
    global user_choice
    user_choice = True

    
def no_button():
    global user_choice
    user_choice = False
    
    
# Popup spell check window
def spell_check(string1, string2, usebool):
    top = Toplevel(root)
    top.geometry("200x120")
    top.title("Spell Check")
    user_choice = False
    spell = Label(top, text="Did you mean?:", relief="flat", font=ft, justify="left")
    spell.place(x=20,y=20,width=100,height=25)
    answer = Label(top, text=string2, relief="flat", font=ft, justify="left")
    answer.place(x=120,y=20,width=100,height=25)
    yes1 = Button(top, text="Yes", command=lambda: [yes_button(), top.destroy()])
    yes1.place(x=20,y=60,width=70,height=25)
    no1 = Button(top, text="No", command=lambda: [no_button(), top.destroy()])
    no1.place(x=110,y=60,width=70,height=25)
    root.wait_window(top)
    

# Function for deleting the password to the local file
def delete_entry():
    # Accountfor case
    if option_var != "":
        user_input = option_var.get()
        user_input = user_input.upper()
        option_var.set(site_option[0])
    elif option_var != "" and for_entry.get() != "":
        user_input = for_entry.get()
        user_input = user_input.upper()
        option_var.set(site_option[0])
    else:
        user_input = for_entry.get()
        user_input = user_input.upper()
    if len(entry.get()) != 0:
        found = False # Boolean for determining if a line exists
        # Read through file line by line
        with open(os.path.join(sys.path[0], "test.txt"), "r") as pf:
            # Stores the line data as strings in the list "Line"
            line = pf.readlines()
            word = []
            # Separate the string stored in the list "line" into "word" list by the ":" delimiter
            for item in line:
                word.append(item.split(":"))
            # Flatten the "word" list
            flatlist=[]
            for sublist in word:
                for element in sublist:
                    flatlist.append(element)
            # Determine if the user has a password saved already then update flatlist
            itvar = 0
            for i in flatlist:
                # Spell Check
                if Levenshtein.ratio(user_input, flatlist[itvar])<1 and Levenshtein.ratio(user_input, flatlist[itvar])>0.4:
                    spell_check(user_input, flatlist[itvar], user_choice)
                    if user_choice == True:
                        user_input = flatlist[itvar]
                if i == user_input:
                    del flatlist[itvar + 1]
                    del flatlist[itvar]
                    found = True
                itvar = itvar + 1
        # Remove the whitespace as it causes a bug
        flatlist = [w.strip(' ') for w in flatlist]
        if found == True:
            # Put it all together into one string then overwrite the file
            file1 = open(os.path.join(sys.path[0], "test.txt"), "w")
            flatlist = ''.join(flatlist)
            file1.write(flatlist)
    # Update text field
    file1 = open(os.path.join(sys.path[0], "test.txt"), "r")
    text.delete("1.0","end")
    for i in file1:
        text.insert(END, i)
    file1.close()


# Function for saving the password to the local file
def update_file():
    # Accountfor case
    if option_var != "":
        user_input = option_var.get()
        user_input = user_input.upper()
        option_var.set(site_option[0])
    elif option_var != "" and for_entry.get() != "":
        user_input = for_entry.get()
        user_input = user_input.upper()
        option_var.set(site_option[0])
    else:
        user_input = for_entry.get()
        user_input = user_input.upper()
    if len(entry.get()) != 0:
        found = False # Boolean for determining if a line exists
        # Read through file line by line
        with open(os.path.join(sys.path[0], "test.txt"), "r") as pf:
            # Stores the line data as strings in the list "Line"
            line = pf.readlines()
            word = []
            # Separate the string stored in the list "line" into "word" list by the ":" delimiter
            for item in line:
                word.append(item.split(":"))
            # Flatten the "word" list
            flatlist=[]
            for sublist in word:
                for element in sublist:
                    flatlist.append(element)
            # Determine if the user has a password saved already then update flatlist
            itvar = 0
            for i in flatlist:
                # Spell Check
                if Levenshtein.ratio(user_input, flatlist[itvar])<1 and Levenshtein.ratio(user_input, flatlist[itvar])>0.4:
                    spell_check(user_input, flatlist[itvar], user_choice)
                    if user_choice == True:
                        user_input = flatlist[itvar]
                if i == user_input:
                    flatlist[itvar + 1] = ":" + entry.get() + "\n"
                    found = True
                # This adds the ":" delimiter back into the second string
                elif (itvar % 2) == 0:
                    flatlist[itvar + 1] = ":" + flatlist[itvar+1]
                itvar = itvar + 1
        # Remove the whitespace as it causes a bug
        flatlist = [w.strip(' ') for w in flatlist]
        if found == True:
            # Put it all together into one string then overwrite the file
            file1 = open(os.path.join(sys.path[0], "test.txt"), "w")
            flatlist = ''.join(flatlist)
            file1.write(flatlist)
        else:
            file1 = open(os.path.join(sys.path[0], "test.txt"), "a")
            file1.write(user_input + ":" + entry.get() + "\n")
            file1.close()
    # Update text field
    file1 = open(os.path.join(sys.path[0], "test.txt"), "r")
    text.delete("1.0","end")
    for i in file1:
        text.insert(END, i)
    file1.close()


# Main Function

# Define variables
w = ""
user_input = ""
user_choice = False
site_option = [
"",
"Amazon",
"Facebook",
"Google",
"Hulu",
"LinkedIn",
"Netflix",
"StackOverflow",
"Yahoo"
]

# Create GUI window
root = Tk()
root.geometry("470x380")
var = IntVar()
var1 = IntVar()
ft = tkFont.Font(family='Times',size=10)
st = tkFont.Font(family='Times',size=12)
option_var = StringVar(root)
option_var.set(site_option[0]) # Default option
 
# Title of your GUI window
root.title("Password Generator v0.2")

# Create a label for what the password is for
f_label = Label(root, text="Site", relief="flat", font=ft, justify="left")
f_label.place(x=20,y=20,width=70,height=25)
option_menu = OptionMenu(root, option_var, *site_option)
option_menu.place(x=100,y=20,width=70,height=25)
for_entry = Entry(root)
for_entry.place(x=190,y=20,width=70,height=25)

# Create label and entry to show the password generated
Random_password = Label(root, text="Password", relief="flat", font=ft, justify="left")
Random_password.place(x=20,y=60,width=70,height=25)
entry = Entry(root)
entry.place(x=100,y=60,width=70,height=25)


# Create label for length of password
c_label = Label(root, text="Length", relief="flat", font=ft, justify="left")
c_label.place(x=20,y=100,width=70,height=25)

# Create the "copy", "generate", and "save" buttons
copy_button = Button(root, text="Copy", command=copy1)
copy_button.place(x=190,y=60,width=70,height=25)
generate_button = Button(root, text="Generate", command=generate)
generate_button.place(x=280,y=60,width=70,height=25)
save_button = Button(root, text="Save", command=update_file)
save_button.place(x=370, y=60, width=70, height=25)
delete_button = Button(root, text="Delete", command=delete_entry)
delete_button.place(x=280, y=20, width=70, height=25)
 
# Radio Buttons for deciding the strength of the password. Default is medium
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.place(x=190,y=100,width=85,height=25)
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.place(x=270,y=100,width=85,height=25)
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.place(x=350,y=100,width=85,height=25)
combo = Combobox(root, textvariable=var1)
 
# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=100,y=100,width=70,height=25)



# Create a text box that shows the currently saved passwords
# Add a Scrollbar(horizontal)
v=Scrollbar(root, orient='vertical')
v.place(x=10,y=1700)


# Add a text widget
text=Text(root, font=("Arial, 12"), yscrollcommand=v.set)

# Create a label for the text box
s_label= Label(root, text="Saved Passwords", relief="flat", font=st, justify="left")
s_label.place(x=10,y=140,width=150,height=25)


# Add some text in the text widget
for i in file1:
   text.insert(END, i)


# Attach the scrollbar with the text widget
v.config(command=text.yview)
text.place(x=10,y=170,width=440,height=195)
 
# start the GUI
root.mainloop()
