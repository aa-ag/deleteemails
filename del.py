import imaplib
import email
from email.header import decode_header
import datetime

'''
Script to delete Gmail emails from inbox
https://docs.python.org/3/library/imaplib.html
'''

username = "[...]"
password = "[...]"

imap = imaplib.IMAP4_SSL("imap.gmail.com")

imap.login(username, password)

imap.select("INBOX")

status, messages = imap.search(None, 'FROM "[...]"')

emails = messages[0].split(b' ')

for email in emails:
    _, msg = imap.fetch(email, "(RFC822)")
    imap.store(email, "+FLAGS", "\\Deleted")

imap.expunge()
imap.close()
imap.logout()