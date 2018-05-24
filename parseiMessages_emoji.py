# Parses iMessages.csv
# message data dump to count
# the number of emoji occurances
import csv
import logging
import os
import json

# Default values
logging.getLogger().setLevel(logging.INFO)

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

# Emojis encoded in utf-8
emoji_encoded_heart_eyes = u'\U0001f60d'.encode('utf-8')
emoji_encoded_grin = u'\U0001f601'.encode('utf-8')
emoji_encoded_amazed = u'\U0001f62e'.encode('utf-8')
emoji_encoded_sobbing = u'\U0001f62d'.encode('utf-8')
emoji_encoded_embarrassed = u'\U0001f605'.encode('utf-8')
emoji_encoded_smile = u'\U0001f60a'.encode('utf-8')
emoji_encoded_pissed = u'\U0001f611'.encode('utf-8')
emoji_encoded_blow_heart_kiss = u'\U0001f618'.encode('utf-8')
emoji_encoded_scream = u'\U0001f631'.encode('utf-8')
emoji_encoded_worried = u'\U0001f628'.encode('utf-8')
emoji_encoded_laughing = u'\U0001f602'.encode('utf-8')
emoji_encoded_sleeping = u'\U0001f634'.encode('utf-8')
emoji_encoded_roll_eyes = u'\U0001f644'.encode('utf-8')
emoji_encoded_lick_lips = u'\U0001f60b'.encode('utf-8')
emoji_encoded_halo = u'\U0001f607'.encode('utf-8')
emoji_encoded_upsidedown = u'\U0001f643'.encode('utf-8')
emoji_encoded_shocked = u'\U0001f633'.encode('utf-8')
emoji_encoded_drool = u'\U0001f924'.encode('utf-8')

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
print('-------------------------------------------------------')
logging.info('Executing parseiMessages_emoji.py')
logging.info('Attempting to open iMessages.csv')
if (os.path.isfile('./iMessages.csv') != True):
    logging.error('Cannot find valid file named: iMessages.csv')
    quit()
else:
    logging.info('Successfully opened iMessages.csv')

# Read in iMessages.csv by the predefined
# column labels
emojis = emojiCounter()
text_messages_read = 0
emojis_found = 0
emojis_in_single_text = 0
most_emojis_found_in_single_text = 0
logging.info('Initializing counters: ' + str(text_messages_read) + ' | ' + str(emojis_found))
dictReader = csv.DictReader(open('iMessages.csv', 'rb'),
fieldnames = ['ROWID', 'text', 'service', 'account', 'date'], delimiter = ',', quotechar = '"')

# Counting each occurance of
# emoji faces in unicode
logging.info('Begin text message analysis')
for row in dictReader:
    text_messages_read += 1
    if (emojis_in_single_text > most_emojis_found_in_single_text):
        most_emojis_found_in_single_text = emojis_in_single_text
    emojis_in_single_text = 0
    for key in row:
        if (key == 'text'):
            singleTextMessage = row[key].decode('utf-8')
            singleTextMessage = singleTextMessage.encode('unicode_escape')
            for word in singleTextMessage.split():
                # Check for heart_eyes emoji
                if (word == emoji_heart_eyes):
                    emojis.heart_eyes += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for grin emoji
                elif (word == emoji_grin):
                    emojis.grin += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for amazed emoji
                elif (word == emoji_amazed):
                    emojis.amazed += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for sobbing emoji
                elif (word == emoji_sobbing):
                    emojis.sobbing += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for embarrassed emoji
                elif (word == emoji_embarrassed):
                    emojis.embarrassed += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for smile emoji
                elif (word == emoji_smile):
                    emojis.smile += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for pissed emoji
                elif (word == emoji_pissed):
                    emojis.pissed += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for blow_heart_kiss emoji
                elif (word == emoji_blow_heart_kiss):
                    emojis.blow_heart_kiss += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for scream emoji
                elif (word == emoji_scream):
                    emojis.scream += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for worried emoji
                elif (word == emoji_worried):
                    emojis.worried += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for laughing emoji
                elif (word == emoji_laughing):
                    emojis.laughing += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for sleeping emoji
                elif (word == emoji_sleeping):
                    emojis.sleeping += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for roll_eyes emoji
                elif (word == emoji_roll_eyes):
                    emojis.roll_eyes += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for lick_lips emoji
                elif (word == emoji_lick_lips):
                    emojis.lick_lips += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for halo emoji
                elif (word == emoji_halo):
                    emojis.halo += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for upsidedown emoji
                elif (word == emoji_upsidedown):
                    emojis.upsidedown += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for shocked emoji
                elif (word == emoji_shocked):
                    emojis.shocked += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
                # Check for drool emoji
                elif (word == emoji_drool):
                    emojis.drool += 1
                    emojis_found += 1
                    emojis_in_single_text += 1
    # Print log messages for single text message line
    logging.info('Text #' + str(text_messages_read))
    logging.info('Emojis in this text: ' + str(emojis_in_single_text))
    logging.info('Total emojis found: ' + str(emojis_found))
    logging.info('-------------------------')
logging.info('Text message analysis complete')

# Creating index.html for emoji visualization
logging.info('Generating index.html file')
html_string = """<html><head><link rel="stylesheet" type="text/css" href="main.css"></head><body>"""
html_string += """<div class = "menu-wrapper"><div class = "menu-title">Emoji Frequency Visualization</div><div class = "data-text">Text Messages Analyzed: """ + str(text_messages_read) + """</div></div><div class = "emoji-wrapper"> """
if emojis.heart_eyes > 0:
    html_string += """<div class = "emoji-heart-eyes">"""
    html_string += emoji_encoded_heart_eyes
    html_string += """</div>"""
if emojis.grin > 0:
    html_string += """<div class = "emoji-grin">"""
    html_string += emoji_encoded_grin
    html_string += """</div>"""
if emojis.amazed > 0:
    html_string += """<div class = "emoji-amazed">"""
    html_string += emoji_encoded_amazed
    html_string += """</div>"""
if emojis.sobbing > 0:
    html_string += """<div class = "emoji-sobbing">"""
    html_string += emoji_encoded_sobbing
    html_string += """</div>"""
# Emoji font sizes over a certain amount will not render
# in Google Chrome v66, this is a known bug
# This should be resolved in v67 (in Beta)
# if emojis.embarrassed > 0:
#     html_string += """<div class = "emoji-embarrassed">"""
#     html_string += emoji_encoded_embarrassed
#     html_string += """</div>"""
if emojis.smile > 0:
    html_string += """<div class = "emoji-smile">"""
    html_string += emoji_encoded_smile
    html_string += """</div>"""
if emojis.pissed > 0:
    html_string += """<div class = "emoji-pissed">"""
    html_string += emoji_encoded_pissed
    html_string += """</div>"""
if emojis.blow_heart_kiss > 0:
    html_string += """<div class = "emoji-blow-heart-kiss">"""
    html_string += emoji_encoded_blow_heart_kiss
    html_string += """</div>"""
if emojis.scream > 0:
    html_string += """<div class = "emoji-scream">"""
    html_string += emoji_encoded_scream
    html_string += """</div>"""
if emojis.worried > 0:
    html_string += """<div class = "emoji-worried">"""
    html_string += emoji_encoded_worried
    html_string += """</div>"""
if emojis.laughing > 0:
    html_string += """<div class = "emoji-laughing">"""
    html_string += emoji_encoded_laughing
    html_string += """</div>"""
if emojis.sleeping > 0:
    html_string += """<div class = "emoji-sleeping">"""
    html_string += emoji_encoded_sleeping
    html_string += """</div>"""
if emojis.roll_eyes > 0:
    html_string += """<div class = "emoji-roll-eyes">"""
    html_string += emoji_encoded_roll_eyes
    html_string += """</div>"""
if emojis.lick_lips > 0:
    html_string += """<div class = "emoji-lick-lips">"""
    html_string += emoji_encoded_lick_lips
    html_string += """</div>"""
if emojis.halo > 0:
    html_string += """<div class = "emoji-halo">"""
    html_string += emoji_encoded_halo
    html_string += """</div>"""
if emojis.upsidedown > 0:
    html_string += """<div class = "emoji-upsidedown">"""
    html_string += emoji_encoded_upsidedown
    html_string += """</div>"""
if emojis.shocked > 0:
    html_string += """<div class = "emoji-shocked">"""
    html_string += emoji_encoded_shocked
    html_string += """</div>"""
if emojis.drool > 0:
    html_string += """<div class = "emoji-drool">"""
    html_string += emoji_encoded_drool
    html_string += """</div>"""
html_string += """</div></body></html>"""
fileHTML = open("index.html","w")
fileHTML.write(html_string)
fileHTML.close()
logging.info('Finished writing to index.html')

# Creating main.css for emoji visualization
logging.info('Generating main.css file')
emoji_size = 2.2
css_string =  """body{width:100%;margin:0px;}"""
css_string += """.emoji-wrapper{padding-left:25px;padding-right: 25px;}"""
css_string += """.menu-wrapper{width:100%;height:100px;background-color:rgb(255,207,0);margin-bottom:25px;}"""
css_string += """.data-text{font-size:15px;position:relative;padding-top:10px;padding-left:40px;color:white;font-family:sans-serif;}"""
css_string += """.menu-title{font-size:30px;position:relative;padding-top:20px;padding-left:20px;color:white;font-family:sans-serif;font-weight:bold;}"""
css_string += """.emoji-heart-eyes{font-size:""" + str(emojis.heart_eyes * emoji_size) + """%;float:left;}"""
css_string += """.emoji-grin{font-size:""" + str(emojis.grin * emoji_size) + """%;float:left;}"""
css_string += """.emoji-amazed{font-size:""" + str(emojis.amazed * emoji_size) + """%;float:left;}"""
css_string += """.emoji-sobbing{font-size:""" + str(emojis.sobbing * emoji_size) + """%;float:left;}"""
css_string += """.emoji-embarrassed{font-size:""" + str(emojis.embarrassed * emoji_size) + """%;float:left;}"""
css_string += """.emoji-smile{font-size:""" + str(emojis.smile * emoji_size) + """%;float:left;}"""
css_string += """.emoji-pissed{font-size:""" + str(emojis.pissed * emoji_size) + """%;float:left;}"""
css_string += """.emoji-blow-heart-kiss{font-size:""" + str(emojis.blow_heart_kiss * emoji_size) + """%;float:left;}"""
css_string += """.emoji-scream{font-size:""" + str(emojis.scream * emoji_size) + """%;float:left;}"""
css_string += """.emoji-worried{font-size:""" + str(emojis.worried * emoji_size) + """%;float:left;}"""
css_string += """.emoji-laughing{font-size:""" + str(emojis.laughing * emoji_size) + """%;float:left;}"""
css_string += """.emoji-sleeping{font-size:""" + str(emojis.sleeping * emoji_size) + """%;float:left;}"""
css_string += """.emoji-roll-eyes{font-size:""" + str(emojis.roll_eyes * emoji_size) + """%;float:left;}"""
css_string += """.emoji-lick-lips{font-size:""" + str(emojis.lick_lips * emoji_size) + """%;float:left;}"""
css_string += """.emoji-halo{font-size:""" + str(emojis.halo * emoji_size) + """%;float:left;}"""
css_string += """.emoji-upsidedown{font-size:""" + str(emojis.upsidedown * emoji_size) + """%;float:left;}"""
css_string += """.emoji-shocked{font-size:""" + str(emojis.shocked * emoji_size) + """%;float:left;}"""
css_string += """.emoji-drool{font-size:""" + str(emojis.drool * emoji_size) + """%;float:left;}"""
fileCSS = open("main.css","w")
fileCSS.write(css_string)
fileCSS.close()
logging.info('Finished writing to main.css')
logging.info('-------------------------')

# Print final log messages
logging.info('Total text messages analyzed: ' + str(text_messages_read))
logging.info('Total emojis found: ' + str(emojis_found))
logging.info('Most emojis found in a single text: ' + str(most_emojis_found_in_single_text))
logging.info('Heart-eyes emojis found: ' + str(emojis.heart_eyes))
logging.info('Grin emojis found: ' + str(emojis.grin))
logging.info('Amazed emojis found: ' + str(emojis.amazed))
logging.info('Sobbing emojis found: ' + str(emojis.sobbing))
logging.info('Embarrassed emojis found: ' + str(emojis.embarrassed))
logging.info('Smile emojis found: ' + str(emojis.smile))
logging.info('Pissed emojis found: ' + str(emojis.pissed))
logging.info('Blow-heart-kiss emojis found: ' + str(emojis.blow_heart_kiss))
logging.info('Scream emojis found: ' + str(emojis.scream))
logging.info('Worried emojis found: ' + str(emojis.worried))
logging.info('Laughing emojis found: ' + str(emojis.laughing))
logging.info('Sleeping emojis found: ' + str(emojis.sleeping))
logging.info('Roll-eyes emojis found: ' + str(emojis.roll_eyes))
logging.info('Lick-lips emojis found: ' + str(emojis.lick_lips))
logging.info('Halo emojis found: ' + str(emojis.halo))
logging.info('Upsidedown emojis found: ' + str(emojis.upsidedown))
logging.info('Shocked emojis found: ' + str(emojis.shocked))
logging.info('drool emojis found: ' + str(emojis.drool))
logging.info('-------------------------')
logging.info('Launching index.html in browser')
logging.info('Finished executing parseiMessages_emoji.py')
print('-------------------------------------------------------')

# Open web page visualization
os.system('open ./index.html')
