import imaplib  # Library for handling Internet Message Access Protocol (IMAP)
import tkinter as tk  # Tkinter for GUI-related tasks such as displaying error messages
from tkinter import messagebox
import email  # Library for handling email messages
from email.message import EmailMessage  # EmailMessage class for creating email messages
from typing import List, Dict, Union  # Type hints for the functions

# Defining the EmailFetcher class
class EmailFetcher:
    # Initialisation method for the EmailFetcher class
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
            
            # Overwrite and delete the password, as it is no longer needed and for extra security ;)
            self.password = None
            del self.password

            return True  # Return True if login was successful
        except imaplib.IMAP4.error:
            return False  # Return False if login failed
    
    # Method for logging out of the user's email session
    def logout(self):
        try:
            # Logout from the IMAP session
            self.mail.logout()
            return True
        except Exception as e:
            print(f"Logout failed: {e}")
            return False
    # Load all emails from the user's email account. Returns a list of dictionaries, where each dictionary represents an email.(Typehint)
    def load_all_emails(self) -> List[Dict[str, Union[str, bool]]]:
        # The IMAP `select` command is used to select the "inbox" mailbox. This is the mailbox from which the emails will be fetched.
        self.mail.select("inbox")
        
        # The IMAP `search` command is used to find all emails in the selected mailbox. The `None` argument means that no specific criteria are used for the search, so all emails will be returned.
        _, data = self.mail.search(None, "ALL")
        
        # The `_fetch_emails` method is called with the email IDs returned by the `search` command. It fetches the emails from the server and returns them as a list of dictionaries.
        return self.fetch_emails(data)

    def fetch_emails(self, data):
        # The input `data` contains a list of email IDs. The first item of the list is split into individual email IDs.
        email_ids = data[0].split()

        # An empty list `emails` is initialised to store the fetched emails.
        emails = []

        # For each email ID in the list of email IDs...
        for email_id in email_ids:
            # the IMAP `fetch` command is used to fetch the email with the given ID. The `BODY.PEEK[]` argument means that the email is fetched without marking it as read.
            _, data = self.mail.fetch(email_id, "(BODY.PEEK[])")
            
            # The raw email data is parsed into an `EmailMessage` object.
            email_message: EmailMessage = email.message_from_bytes(data[0][1])
            
            # The `_parse_email` method is called with the `EmailMessage` object to convert the email into a more usable dictionary format.
            #email_dict = self._parse_email(email_message)
            
            # The dictionary representing the email is appended to the list of emails.
            emails.append(email_message)

        # The list of emails is returned.
        return emails

    