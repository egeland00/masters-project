import tkinter as tk
from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttkbs
from ttkbootstrap import *


root = ttkbs.Window(themename="superhero")

loginbutton = ttkbs.Button(root, text="Login", bootstyle=SUCCESS)
loginbutton.pack(side=LEFT, padx=5, pady=10)

checkbutton = ttkbs.Checkbutton(root, text="Terms of Agreement", style="success")
checkbutton.pack(side=LEFT, padx=5, pady=10)

root.mainloop()
