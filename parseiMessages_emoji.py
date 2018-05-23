# Parses iMessages.csv
# message data dump to count
# the number of emoji occurances
#
import csv
import logging
import os
import re

# emoji unicode text that
# is being searched/counted
emoji_heart_eyes = "\U0001f60d"
emoji_grin = "\U0001f601"
emoji_amazed = "\U0001f62e"
emoji_sobbing = "\U0001f62d"
emoji_embarrassed = "\U0001f605"
emoji_smile = "\U0001f60a"
emoji_pissed = "\U0001f611"
emoji_blow_heart_kiss = "\U0001f618"
emoji_scream = "\U0001f631"
emoji_worried = "\U0001f628"
emoji_laughing = "\U0001f602"
emoji_sleeping = "\U0001f634"
emoji_roll_eyes = "\U0001f644"
emoji_lick_lips = "\U0001f60b"
emoji_halo = "\U0001f607"
emoji_upsidedown = "\U0001f643"
emoji_shocked = "\U0001f633"
emoji_drool = "\U0001f924"

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
        self.blow_heart_kiss = 0
        self.scream = 0
        self.worried = 0
        self.laughing = 0
        self.sleeping = 0
        self.roll_eyes = 0
        self.lick_lips = 0
        self.halo = 0
        self.upsidedown = 0
        self.shocked = 0
        self.drool = 0

# Check if iMessages.csv file exists
if (os.path.isfile('./iMessages.csv') != True):
    logging.error('Cannot find valid file named: iMessages.csv')
    quit()

# Read in iMessages.csv by the predefined
# column labels
emojis = emojiCounter()
dictReader = csv.DictReader(open('iMessages.csv', 'rb'),
fieldnames = ['ROWID', 'text', 'service', 'account', 'date'], delimiter = ',', quotechar = '"')

# Counting each occurance of
# emoji faces in unicode
for row in dictReader:
    for key in row:
        if (key == 'text'):
            singleTextMessage = row[key].decode('utf-8')
            singleTextMessage = singleTextMessage.encode('unicode_escape')
            for word in singleTextMessage.split():
                # Check for 😍 emoji
                if (word == emoji_heart_eyes):
                    emojis.heart_eyes += 1
                # Check for 😁 emoji
                elif (word == emoji_grin):
                    emojis.grin += 1
                # Check for 😮 emoji
                elif (word == emoji_amazed):
                    emojis.amazed += 1
                # Check for 😭 emoji
                elif (word == emoji_sobbing):
                    emojis.sobbing += 1
                # Check for 😅 emoji
                elif (word == emoji_embarrassed):
                    emojis.embarrassed += 1
                # Check for 😊 emoji
                elif (word == emoji_smile):
                    emojis.smile += 1
                # Check for 😑 emoji
                elif (word == emoji_pissed):
                    emojis.pissed += 1
                # Check for 😘 emoji
                elif (word == emoji_blow_heart_kiss):
                    emojis.blow_heart_kiss += 1
                # Check for 😱 emoji
                elif (word == emoji_scream):
                    emojis.scream += 1
                # Check for 😨 emoji
                elif (word == emoji_worried):
                    emojis.worried += 1
                # Check for 😂 emoji
                elif (word == emoji_laughing):
                    emojis.laughing += 1
                # Check for 😴 emoji
                elif (word == emoji_sleeping):
                    emojis.sleeping += 1
                # Check for 🙄 emoji
                elif (word == emoji_roll_eyes):
                    emojis.roll_eyes += 1
                # Check for 😋 emoji
                elif (word == emoji_lick_lips):
                    emojis.lick_lips += 1
                # Check for 😇 emoji
                elif (word == emoji_halo):
                    emojis.halo += 1
                # Check for 🙃 emoji
                elif (word == emoji_upsidedown):
                    emojis.upsidedown += 1
                # Check for 😳 emoji
                elif (word == emoji_shocked):
                    emojis.shocked += 1
                # Check for 🤤 emoji
                elif (word == emoji_drool):
                    emojis.drool += 1