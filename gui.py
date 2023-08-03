import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as ttkbs
from ttkbootstrap import *


#Making window using ttkbootstrap (theme = superhero)
root = ttkbs.Window(themename="superhero")
root.title("Phishing Detection")
root.geometry("1920x1080")

#Creating a Frame to hold the widgets in center of window
frame = ttkbs.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add a header label
header = ttkbs.Label(frame, text="Welcome to Phishing Detection(EDUCATIONAL PURPOSE ONLY)", style="info", font=("Ubuntu", 24, "bold"))
header.grid(column=0, row=0, padx=5, pady=10)

#Terms of Agreement button and function to show terms
def show_terms():
    with open('/home/orjan/Documents/GitHub/masters-project/TOA.txt', 'r') as f:
        terms = f.read()
    messagebox.showinfo("Terms of Agreement", terms)

#Terms of Agreement button and function to show terms
checkbutton = ttkbs.Checkbutton(frame, text="Terms of Agreement", style="secondary", command=show_terms)
checkbutton.grid(column=0, row=6, padx=5, pady=10)

# Email and password entry labels and entry fields
email_label = ttkbs.Label(frame, text="Email", style="info")
email_label.grid(column=0, row=1, padx=5, pady=10)
email_entry = ttkbs.Entry(frame, width=30, style="info")
email_entry.grid(column=0, row=2, padx=5, pady=10)

password_label = ttkbs.Label(frame, text="Password", style="info")
password_label.grid(column=0, row=3, padx=5, pady=10)
password_entry = ttkbs.Entry(frame, width=30, style="info")
password_entry.grid(column=0, row=4, padx=5, pady=10)

#Login button
loginbutton = ttkbs.Button(frame, text="Login", bootstyle=SUCCESS)
loginbutton.grid(column=0, row=5, pady=10)

root.mainloop()

