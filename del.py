import imaplib
import datetime

'''
Script to delete Gmail emails from inbox
https://docs.python.org/3/library/imaplib.html
'''

inbox = imaplib.IMAP4_SSL('imap.gmail.com')

print("{0} Connecting to mailbox via IMAP...".format(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
inbox.login("[...]", "[...]")

inbox.select('[Gmail]/Promotions')

typ, data = inbox.search(None, 'ALL')

inbox.select('[Gmail]/Trash')

for num in data[0].split():
    inbox.store(num, '+FLAGS', '\\Deleted')

inbox.expunge()

inbox.close()
inbox.logout()

print('All done.')