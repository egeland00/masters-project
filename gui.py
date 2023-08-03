# Importing required libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as ttkbs
from ttkbootstrap import *

# Defining the GUI class for the application
class PhishingDetectorGUI:
    def __init__(self):
        # Creating the main application window with a title and fixed geometry.
        self.root = ttkbs.Window(themename="superhero")
        self.root.title("Phishing Detection")
        self.root.geometry("1920x1080")

        # Creating a Frame to hold the widgets in the center of the window
        self.frame = ttkbs.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Adding a header label to the GUI
        self.header = ttkbs.Label(self.frame, text="Welcome to Phishing Detection(EDUCATIONAL PURPOSE ONLY)", style="info", font=("Ubuntu", 24, "bold"))
        self.header.grid(column=0, row=0, padx=5, pady=10)

        # Adding a checkbutton for terms of agreement and linking it to the 'show_terms' function
        self.checkbutton = ttkbs.Checkbutton(self.frame, text="Terms of Agreement", style="secondary", command=self.show_terms)
        self.checkbutton.grid(column=0, row=8, padx=5, pady=10)

        # Adding labels and entry fields for Email and Password
        self.email_label = ttkbs.Label(self.frame, text="Email", style="info")
        self.email_label.grid(column=0, row=1, padx=5, pady=10)
        self.email_entry = ttkbs.Entry(self.frame, width=30, style="info")
        self.email_entry.grid(column=0, row=2, padx=5, pady=10)
        
        self.password_label = ttkbs.Label(self.frame, text="Password", style="info")
        self.password_label.grid(column=0, row=3, padx=5, pady=10)
        self.password_entry = ttkbs.Entry(self.frame, width=30, style="info")
        self.password_entry.grid(column=0, row=4, padx=5, pady=10)

        # Adding a combobox for choosing the email client
        self.server_label = ttkbs.Label(self.frame, text="Choose Email Client", style="info")
        self.server_label.grid(column=0, row=5, padx=5, pady=10)
        self.server_combobox = ttkbs.Combobox(self.frame, width=27, style="info")
        self.server_combobox['values'] = ('Outlook (Working)', 'Gmail (Not Working)', 'Others (Not Working)')
        self.server_combobox.grid(column=0, row=6, padx=5, pady=10)

        # Adding a Login button
        self.loginbutton = ttkbs.Button(self.frame, text="Login", bootstyle='success')
        self.loginbutton.grid(column=0, row=7, pady=10)

    # Function to read and display the terms of agreement
    def show_terms(self):
        with open('/home/orjan/Documents/GitHub/masters-project/TOA.txt', 'r') as f:
            terms = f.read()
        messagebox.showinfo("Terms of Agreement", terms)

    # Function to start the GUI
    def run(self):
        self.root.mainloop()

# Creating an instance of the GUI and running it
if __name__ == "__main__":
    app = PhishingDetectorGUI()
    app.run()
