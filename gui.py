import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as ttkbs
from ttkbootstrap import *


#Making window using ttkbootstrap (theme = superhero)
root = ttkbs.Window(themename="superhero")

#Login button
loginbutton = ttkbs.Button(root, text="Login", bootstyle=SUCCESS)
loginbutton.pack(side=LEFT, padx=5, pady=10)

#Terms of Agreement button and fucntion to show terms
def show_terms():
    with open('/home/orjan/Documents/GitHub/masters-project/TOA.txt', 'r') as f:
        terms = f.read()
    messagebox.showinfo("Terms of Agreement", terms)

#Terms of Agreement button and function to show terms
checkbutton = ttkbs.Checkbutton(root, text="Terms of Agreement", style="secondary", command=show_terms)
checkbutton.pack(side=tk.LEFT, padx=5, pady=10)



root.mainloop()
