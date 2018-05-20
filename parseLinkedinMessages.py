# Parses Inbox.csv Linkedin
# message data dump to create an
# output file in the following format:
#
# Message: text text text text
# Reponse: text text text text
import csv
import logging
import os

# Message object defining
# how we will store table data
class Message():
    def __init__(self):
        self.messageFrom = ''
        self.messageTo = ''
        self.messageContent = ''

    def addFrom(self, messageFrom):
        self.messageFrom = messageFrom

    def addTo(self, messageTo):
        self.messageTo = messageTo

    def addContent(self, messageContent):
        self.messageContent = messageContent

# Check if Inbox.csv file exists
if (os.path.isfile('./Inbox.csv') != True):
    logging.error('Cannot find valid file named: Inbox.csv')
    quit()

# Get the name of the user
# as it will appear in their
# logged messages
personName = raw_input('Enter your full Linkedin account name: ')
messages = []

# Read in Inbox.csv by the predefined
# column labels
dictReader = csv.DictReader(open('Inbox.csv', 'rb'),
fieldnames = ['From', 'To', 'Date', 'Subject', 'Content', 'Direction', 'Folder'], delimiter = ',', quotechar = '"')

# Adding each Inbox.csv message to messages[]
for row in dictReader:
    for key in row:
        message = Message()
        if (key == 'From'):
            message.addFrom(row[key])
        elif (key == 'To'):
            message.addTo(row[key])
        elif (key == 'Content'):
            message.addContent(row[key])
        # Add new message to messages array
        messages.append(message)
