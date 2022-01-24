import csv
rows = []
with open("username.csv","r") as file:


# type(file)
   csvreader = csv.reader(file)

   header = next(csvreader)
   for row in csvreader:
       rows.append(row)
print(header)
print(rows)