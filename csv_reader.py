import csv

with open('country-list.csv', 'r') as csvfile:
   reader = csv.reader(csvfile)
   sorted_rows = sorted(reader, key=lambda row: row[0])  
   for row in sorted_rows: 
       print(row)
