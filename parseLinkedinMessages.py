# Parses Inbox.csv Linkedin
# message data dump to create an
# output file in the following format:
import csv
import logging
import os
import numpy as np

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
combinedDictionary = {}

# Read in Inbox.csv by the predefined
# column labels
dictReader = csv.DictReader(open('Inbox.csv', 'rb'),
fieldnames = ['From', 'To', 'Date', 'Subject', 'Content', 'Direction', 'Folder'], delimiter = ',', quotechar = '"')

# Adding each Inbox.csv message to messages[]
for row in dictReader:
    message = Message()
    for key in row:
        if (key == 'From'):
            message.addFrom(row[key])
        elif (key == 'To'):
            message.addTo(row[key])
        elif (key == 'Content'):
            message.addContent(row[key])
    # Add new message to messages array
    messages.append(message)

# Create output file composed of
# messages and responses
# Message: text text text text
# Reponse: text text text text
messageResponseString = ""
messageResponseDictionary = ""
currentMessageString = ""
responseDictionary = dict()
senderToggle = True
for message in messages:
    if (message.messageContent != ""):
        if (message.messageTo == personName and message.messageFrom != "" and senderToggle == True):
            messageResponseString += "Message: " + message.messageContent + "\n"
            messageResponseDictionary += "(" + message.messageContent + ","
            currentMessageString = message.messageContent
            senderToggle = False
        elif (message.messageFrom == personName and message.messageTo != "" and senderToggle == False):
            messageResponseString += "Response: " + message.messageContent + "\n"
            messageResponseDictionary += message.messageContent + ")\n"
            responseDictionary[message.messageContent] = currentMessageString
            senderToggle = True

# Generating conversationData.txt
conversationDataFile = open("conversationData.txt","w")
conversationDataFile.write(messageResponseString)
conversationDataFile.close()

# Create output file of message pairs
# (FRIENDS_MESSAGE, YOUR_RESPONSE)
combinedDictionary.update(responseDictionary)
np.save('conversationDictionary.npy', combinedDictionary)
# conversationDictionaryFile = open("conversationDictionary.npy","w")
# conversationDictionaryFile.write(messageResponseDictionary)
# conversationDictionaryFile.close()
