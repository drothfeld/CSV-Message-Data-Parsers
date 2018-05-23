# Parses iMessages.csv
# message data dump to count
# the number of emoji occurances
#
import csv
import logging
import os
import re

# emojiCounter object defining
# how we will count emojis
class emojiCounter():
    def __init__(self):
        self.heart_eyes = 0
        self.grin = 0
        self.amazed = 0
        self.sobbing = 0
        self.embarrassed = 0
        self.smile = 0
        self.pissed = 0
        self.tongue = 0
        self.blow_heart_kiss = 0
        self.scream = 0
        self.worried = 0
        self.laughing = 0
        self.sleeping = 0
        self.roll_eyes = 0
        self.lick_lips = 0

# Check if Inbox.csv file exists
if (os.path.isfile('./iMessages.csv') != True):
    logging.error('Cannot find valid file named: iMessages.csv')
    quit()

# Read in iMessages.csv by the predefined
# column labels
emojis = emojiCounter()
dictReader = csv.DictReader(open('iMessages.csv', 'rb'),
fieldnames = ['ROWID', 'text', 'service', 'account', 'date'], delimiter = ',', quotechar = '"')

# Counting each occurance of
# emoji faces
for row in dictReader:
    for key in row:
        if (key == 'text'):
            singleTextMessage = row[key].decode('utf-8')
            singleTextMessage = singleTextMessage.encode('unicode_escape')
            for word in singleTextMessage.split():
                print (word)
