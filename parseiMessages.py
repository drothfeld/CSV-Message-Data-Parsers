# Parses iMessages.csv
# message data dump to count
# the number of emoji occurances
import csv
import logging
import os
import json

# Default values
logging.getLogger().setLevel(logging.INFO)
combinedDictionary = {}

# Check if iMessages.csv file exists
if (os.path.isfile('./iMessages.csv') != True):
    logging.error('Cannot find valid file named: iMessages.csv')
    quit()

# Read in iMessages.csv by the predefined
# column labels
messages = []
dictReader = csv.DictReader(open('iMessages.csv', 'rb'),
fieldnames = ['ROWID', 'text', 'service', 'account', 'date'], delimiter = ',', quotechar = '"')

# Parsing through iMessages.csv to get
# messages and responses
for row in dictReader:
    for key in row:
        if (key == 'text'):
            if (row[key] != "NULL" and row[key] != ""):
                messages.append(row[key])

# Create output file composed of
# messages and responses
# Message: text text text text
# Reponse: text text text text
messageResponseDictionary = ""
messageResponseString = ""
currentMessageString = ""
responseDictionary = dict()
senderToggle = True
for message in messages:
    if (senderToggle == True):
        messageResponseString += "Message: " + message + "\n"
        messageResponseDictionary += "(" + message + ","
        currentMessageString = message
        senderToggle = False
    else:
        messageResponseString += "Response: " + message + "\n"
        messageResponseDictionary += message + ")\n"
        responseDictionary[message] = currentMessageString
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
