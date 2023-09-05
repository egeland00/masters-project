# Importing required libraries
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as ttkbs
from email_fetcher import EmailFetcher
from typing import List, Dict, Union
from email_scanner import EmailScanner

# Defining the GUI class for the application
class PhishingDetectorGUI:
    def __init__(self):
        # Creating the main application window with a title and fixed geometry.
        self.root = ttkbs.Window(themename="superhero")
        self.root.title("Phishing Detection")
        self.root.geometry("1920x1080")
        self.scanner = EmailScanner('/home/orjan/Documents/GitHub/masters-project/dataset.csv')
        self.create_login_frame()  # Creating the login frame
    
    def create_login_frame(self):
        # Creating a Frame to hold the widgets in the center of the window
        self.login_frame = ttkbs.Frame(self.root)
        self.login_frame.pack(expand=True)

        # Adding a header label to the GUI
        self.header = ttkbs.Label(self.login_frame, text="Welcome to Phishing Detection(EDUCATIONAL PURPOSE ONLY)", bootstyle="default", font=("Ubuntu", 24, "bold"))
        self.header.pack(padx=5, pady=10)

        # Adding labels and entry fields for Email
        self.email_label = ttkbs.Label(self.login_frame, text="Email", style="info")
        self.email_label.pack(padx=5, pady=10)
        self.email_entry = ttkbs.Entry(self.login_frame, width=30, style="info")
        self.email_entry.pack(padx=5, pady=10)

        # Adding labels and entry fields for Password
        self.password_label = ttkbs.Label(self.login_frame, text="Password", style="info")
        self.password_label.pack(padx=5, pady=10)
        self.password_entry = ttkbs.Entry(self.login_frame, width=30, style="info", show="*")
        self.password_entry.pack(padx=5, pady=10)

        # Adding a combobox for choosing the email client
        self.server_label = ttkbs.Label(self.login_frame, text="Choose Email Client", style="info")
        self.server_label.pack(padx=5, pady=10)
        self.server_combobox = ttkbs.Combobox(self.login_frame, width=27, style="info")
        self.server_combobox['values'] = ('Outlook (Working)', 'Gmail (Not Working)', 'Others (Not Working)')
        self.server_combobox.pack(padx=5, pady=10)

        # Adding a Login button and linking it to the 'login' function
        self.loginbutton = ttkbs.Button(self.login_frame, text="Login", bootstyle='success', command=self.login)
        self.loginbutton.pack(pady=10)

        # Adding a checkbutton for terms of agreement and linking it to the 'show_terms' function
        self.checkbutton = ttkbs.Checkbutton(self.login_frame, text="Terms of Agreement", style="info", command=self.show_terms)
        self.checkbutton.pack(padx=5, pady=10)

    
    
    def create_main_frame(self):
        # Create a new Frame widget that will hold all other widgets. This frame is placed in the center of the root window.
        self.main_frame = ttkbs.Frame(self.root)
        self.main_frame.pack(expand=True)

        # Create a label with a welcome message. This label is packed at the top of the frame.
        self.header = ttkbs.Label(self.main_frame, text="Welcome to MSC Email Phishing Detector", bootstyle="default", font=("Ubuntu", 24, "bold"))
        self.header.pack(padx=5, pady=10)

        self.info_header = ttkbs.Label(self.main_frame, text="Step by Step:\n 1. Load Your Emails By Pressing 'Load Emails' \n 2. Scan Emails By Pressing 'Scan Now' \n 3. View Results", bootstyle="info", font=("Ubuntu", 12))
        self.info_header.pack(padx=5, pady=10)
        # Create a Treeview to display the emails. It has five columns: From, To, Date, Subject, and Risk.
        self.email_treeview = ttkbs.Treeview(self.main_frame, columns=("From", "To", "Date", "Subject", "Risk"), show='headings', height=25)
        # Set the headings for each column in the Treeview.
        self.email_treeview.heading("From", text="From")
        self.email_treeview.heading("To", text="To")
        self.email_treeview.heading("Date", text="Date")
        self.email_treeview.heading("Subject", text="Subject")
        self.email_treeview.heading("Risk", text="Risk")
        self.email_treeview.pack(pady=5)

        # Create a Frame to hold the buttons on left side.
        left_button_frame = ttkbs.Frame(self.main_frame)
        left_button_frame.pack(side='left') 

        # Create a Frame to hold the buttons on right side.
        right_button_frame = ttkbs.Frame(self.main_frame)
        right_button_frame.pack(side='right')

        # Create a "Scan Now" button with a green color (success style). This button is packed to the left in the button frame.
        scan_emails_button = ttkbs.Button(left_button_frame, text="Scan Now", style="success", command=self.scan_emails)
        scan_emails_button.pack(side='left', padx= 10, pady=5)

        # Create a "Load Emails" button with a blue color (info style). This button is packed to the left in the button frame, next to the "Scan Now" button.
        load_all_emails_button = ttkbs.Button(left_button_frame, text="Load Emails", style="info", command=self._all_emails)
        load_all_emails_button.pack(side='left', padx= 10, pady=5)

        # Create a "Logout" button with an orange color (warning style). This button is packed to the right in the button frame.
        logout_button = ttkbs.Button(right_button_frame, text="Logout", style="warning", command=self.logout)
        logout_button.pack(side='right', padx=10, pady=5)



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
            self.create_main_frame() # Show the main frame
            messagebox.showinfo("Success", "Logged in successfully!")
        else:
            messagebox.showerror("Error", "Incorrect Credentials!")

    # Function to read and display the terms of agreement
    def show_terms(self):
        with open('/home/orjan/Documents/GitHub/masters-project/TOA.txt', 'r') as f:
            terms = f.read()
        messagebox.showinfo("Terms of Agreement", terms)

    # Function to handle logout, calling the logout function in the EmailFetcher class
    def logout(self):
        if self.email_fetcher.logout():
            messagebox.showinfo("Success", "Logged out successfully!")
        else:
            messagebox.showerror("Error", "Logout failed!")
        
        # Destroing the main frame and recreate the login frame
        self.main_frame.destroy()
        self.create_login_frame()  

    # The function "_all_emails" fetches all emails from the email account associated with the email fetcher object.
    # It then uses these emails to update the GUI's email table.
    def _all_emails(self):
        # Retrieve all emails from the email account. Function is called from email_fetcher.py
        emails = self.email_fetcher.load_all_emails()
        # Update the email table in the GUI with the fetched emails
        self.update_table(emails)

    

    # The function "_update_table" takes a list of emails (each email represented as a dictionary) as input.
    # It updates the GUI's email table with these emails.
    def update_table(self, emails: List[Dict[str, Union[str, bool]]]) -> None:
        # Initialise a list to store the IDs of the email entries in the table
        self.email_ids = []    

        # Clear the email table by deleting all current entries
        for email in self.email_treeview.get_children():
            self.email_treeview.delete(email)
        
        # For each email in the input list, insert a new entry in the email table
        for email in emails:
            # Check if the email is classified as phishing (according to the "is_phishing" key in the email dictionary).
            # If it is, set the tag for this email entry to "spam". If it's not, set the tag to "not_spam".
            if email.get("is_phishing", False):
                tag = "spam"
            else:
                tag = "not_spam"
            
            # Insert a new entry at the end of the email table. The entry's values are the email's information.
            # Also, assign the previously determined tag to this entry.
            email_id = self.email_treeview.insert('', 'end', values=(
                email['from'],   
                email['to'],     
                email['date'],   
                email['subject'],
                'yes' if email.get("is_phishing", False) else 'no'  # Whether the email is classified as phishing
            ), tags=(tag,))  # Tag indicating whether the email is classified as phishing
            
            # Add the ID of the new entry to the list of email IDs
            self.email_ids.append(email_id)
        self.email_treeview.tag_configure("spam", background="red")  # Set the background color of the "spam" tag to red
        self.email_treeview.tag_configure("not_spam", background="green")  # Set the background color of the "not_spam" tag to green
    
    # Function to handle the "Scan Now" button
    def scan_emails(self):
        emails = self.email_fetcher.load_all_emails()
        # Scan emails for phishing
        for i, email in enumerate(emails):
            if isinstance(email["body"], bool):
                continue
            result = self.scanner.scan(str(email["body"]))
            print(f"Email {i+1} scan result: {result}")  # Print the result of the scan, for debugging purposes
            email["is_phishing"] = result
            if email["is_phishing"] == 'spam':
                self.email_treeview.item(self.email_ids[i], tags='spam') 
            else:
                self.email_treeview.item(self.email_ids[i], tags='not_spam')

        self.email_treeview.tag_configure('spam', background='red')
        self.email_treeview.tag_configure('not_spam', background='green')    

        print("Scanning emails completed.")
        messagebox.showinfo("Info", "Scanning emails completed.")

        # Update table with new emails
        self.update_table(emails)

    # Function to start the GUI
    def run(self):
        self.root.mainloop()

#Creating an instance of the GUI and running it
if __name__ == "__main__":
    app = PhishingDetectorGUI()
    app.run()
