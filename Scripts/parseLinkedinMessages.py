import csv
d = {}
d['From'] = []
d['To'] = []
d['Date'] = []
d['Subject'] = []
d['Content'] = []
d['Direction'] = []
d['Folder'] = []

dictReader = csv.DictReader(open('Inbox.csv', 'rb'),
fieldnames = ['From',
              'To',
              'Date',
              'Subject',
              'Content',
              'Direction',
              'Folder'],
delimiter = ',', quotechar = '"')

for row in dictReader:
    for key in row:
        d[key].append(row[key])

print(d['From'])
