# Parses Inbox.csv Linkedin
# message data dump to create an
# output file in the following format:
#
# Message: text text text text
# Reponse: text text text text
import csv
import logging
import os

# Check if Inbox.csv file exists
if (os.path.isfile('./Inbox.csv') != True):
    logging.error('Cannot find valid file named: Inbox.csv')
    quit()

personName = raw_input('Enter your full Linkedin account name: ')

# Column data should be organized by
# these labels in Inbox.csv
columnData = {}
columnData['From'] = []
columnData['To'] = []
columnData['Date'] = []
columnData['Subject'] = []
columnData['Content'] = []
columnData['Direction'] = []
columnData['Folder'] = []

# Read in Inbox.csv by the predefined
# column labels
dictReader = csv.DictReader(open('Inbox.csv', 'rb'),
fieldnames = ['From', 'To', 'Date', 'Subject', 'Content', 'Direction', 'Folder'], delimiter = ',', quotechar = '"')

# Adding all Inbox.csv rows to columnData
for row in dictReader:
    for key in row:
        columnData[key].append(row[key])

# for message in columnData['From']:
#     print(message)
