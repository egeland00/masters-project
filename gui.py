# Importing required libraries
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as ttkbs
from email_fetcher import EmailFetcher

# Defining the GUI class for the application
class PhishingDetectorGUI:
    def __init__(self):
        # Creating the main application window with a title and fixed geometry.
        self.root = ttkbs.Window(themename="superhero")
        self.root.title("Phishing Detection")
        self.root.geometry("1920x1080")
        
        self._create_login_frame()  # Creating the login frame
    
    def _create_login_frame(self):
        # Creating a Frame to hold the widgets in the center of the window
        self.login_frame = ttkbs.Frame(self.root)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Adding a header label to the GUI
        self.header = ttkbs.Label(self.login_frame, text="Welcome to Phishing Detection(EDUCATIONAL PURPOSE ONLY)", bootstyle="default", font=("Ubuntu", 24, "bold"))
        self.header.grid(column=0, row=0, padx=5, pady=10)

        # Adding a checkbutton for terms of agreement and linking it to the 'show_terms' function
        self.checkbutton = ttkbs.Checkbutton(self.login_frame, text="Terms of Agreement", style="info", command=self.show_terms)
        self.checkbutton.grid(column=0, row=8, padx=5, pady=10)

        # Adding labels and entry fields for Email and Password
        self.email_label = ttkbs.Label(self.login_frame, text="Email", style="info")
        self.email_label.grid(column=0, row=1, padx=5, pady=10)
        self.email_entry = ttkbs.Entry(self.login_frame, width=30, style="info")
        self.email_entry.grid(column=0, row=2, padx=5, pady=10)
        
        self.password_label = ttkbs.Label(self.login_frame, text="Password", style="info")
        self.password_label.grid(column=0, row=3, padx=5, pady=10)
        self.password_entry = ttkbs.Entry(self.login_frame, width=30, style="info")
        self.password_entry.grid(column=0, row=4, padx=5, pady=10)

        # Adding a combobox for choosing the email client
        self.server_label = ttkbs.Label(self.login_frame, text="Choose Email Client", style="info")
        self.server_label.grid(column=0, row=5, padx=5, pady=10)
        self.server_combobox = ttkbs.Combobox(self.login_frame, width=27, style="info")
        self.server_combobox['values'] = ('Outlook (Working)', 'Gmail (Not Working)', 'Others (Not Working)')
        self.server_combobox.grid(column=0, row=6, padx=5, pady=10)

        # Adding a Login button and linking it to the 'login' function
        self.loginbutton = ttkbs.Button(self.login_frame, text="Login", bootstyle='success', command=self.login)
        self.loginbutton.grid(column=0, row=7, pady=10)
    
    
    def _create_main_frame(self):
        # Create a new Frame widget that will hold all other widgets. This frame is placed in the center of the root window.
        self.main_frame = ttkbs.Frame(self.root)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a label with a welcome message. This is placed in the top row of the grid within the frame.
        self.header = ttkbs.Label(self.main_frame, text="Welcome! Start by loading emails followed by scan", bootstyle="default", font=("Ubuntu", 24, "bold"))
        self.header.grid(column=0, row=0, padx=5, pady=10)

        # Create a "Scan Now" button with a green color (success style). This button is placed next to the label.
        scan_emails_button = ttkbs.Button(self.main_frame, text="Scan Now", style="success")
        scan_emails_button.grid(column=0, row=1, padx=10, pady=5)

        # Create a "Load Emails" button with a blue color (info style). This button is placed next to the "Scan Now" button.
        load_all_emails_button = ttkbs.Button(self.main_frame, text="Load Emails", style="info")
        load_all_emails_button.grid(column=1, row=1, padx=10, pady=5)

        # Create a "Logout" button with an orange color (warning style). This button is placed next to the "Load Emails" button.
        logout_button = ttkbs.Button(self.main_frame, text="Logout", style="warning")
        logout_button.grid(column=2, row=1, padx=10, pady=5)

        # Create a Treeview to display the emails. It has five columns: From, To, Date, Subject, and Risk.
        self.email_treeview = ttkbs.Treeview(self.main_frame, columns=("From", "To", "Date", "Subject", "Risk"), show='headings')
        # Set the headings for each column in the Treeview.
        self.email_treeview.heading("From", text="From")
        self.email_treeview.heading("To", text="To")
        self.email_treeview.heading("Date", text="Date")
        self.email_treeview.heading("Subject", text="Subject")
        self.email_treeview.heading("Risk", text="Risk")
        # Place the Treeview below the buttons in the grid.
        self.email_treeview.grid(column=0, row=3, columnspan=3, sticky='nsew')

        # Function to handle login
    def login(self):
        # Get email, password and email service from the fields
        email = self.email_entry.get()
        password = self.password_entry.get()
        email_service = self.server_combobox.get()
        
        # Create EmailFetcher instance
        self.email_fetcher = EmailFetcher(email, password, email_service)
        if self.email_fetcher.login():
            self.login_frame.destroy()  # Hide the login frame
            self._create_main_frame() # Show the main frame
            messagebox.showinfo("Success", "Logged in successfully!")
        else:
            messagebox.showerror("Error", "Incorrect Credentials!")

    # Function to read and display the terms of agreement
    def show_terms(self):
        with open('/home/orjan/Documents/GitHub/masters-project/TOA.txt', 'r') as f:
            terms = f.read()
        messagebox.showinfo("Terms of Agreement", terms)

    # Function to start the GUI
    def run(self):
        self.root.mainloop()

#Creating an instance of the GUI and running it
if __name__ == "__main__":
    app = PhishingDetectorGUI()
    app.run()
