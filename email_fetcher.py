import imaplib  # Library for handling Internet Message Access Protocol (IMAP)
import tkinter as tk  # Tkinter for GUI-related tasks such as displaying error messages
from tkinter import messagebox

# Defining the EmailFetcher class
class EmailFetcher:
    # Initialization method for the EmailFetcher class
    def __init__(self, email: str, password: str, email_service: str):
        self.email = email  # User's email
        self.password = password  # User's password
        self.email_service = email_service  # User's email service
        self.imap_server = None  # Placeholder for IMAP server address
        self.mail = None  # Placeholder for IMAP mail object

    # Method for logging into the user's email account
    def login(self) -> bool:
        # Determine the IMAP server based on the provided email service
        if self.email_service == "Gmail (Not Working)":
            self.imap_server = "imap.gmail.com"  # IMAP server for Gmail
        elif self.email_service == "Outlook (Working)":
            self.imap_server = "outlook.office365.com"  # IMAP server for Outlook
        else:
            # Raise an error if an unsupported email service is provided
            raise ValueError("Invalid email service")

        try:
            # Create an IMAP4 class with SSL 
            self.mail = imaplib.IMAP4_SSL(self.imap_server)
            # Perform the login using the provided email and password
            self.mail.login(self.email, self.password)
            return True  # Return True if login was successful
        except imaplib.IMAP4.error as e:
            # Print the error if login failed and show an error message to the user
            messagebox.showerror("Error", "Incorrect Credentials!")
            return False  # Return False if login failed
