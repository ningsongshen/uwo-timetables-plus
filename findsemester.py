import csv, re
# import re
# import pandas as pd
# csv_input = pd.read_csv('data/all.csv')
# csv_input['suffix'] = csv_input[0].
# csv_input.to_csv('data/all1.csv')
with open('data/all.csv', newline='') as csvfile:
    freader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('data/allsem.csv', 'w', newline='') as outfile:
        owriter = csv.writer(outfile)
        for row in freader:
            course = row[0]
            match = re.search(r'\d\d\d\d.', course)
            code = match.group(0)[4]
            if code == " ":
                code = "*"
            row.insert(0, code)
            owriter.writerow(row)

