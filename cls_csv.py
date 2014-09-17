import csv
with open('example.csv') as csvfile:
  data = csv.reader(csvfile, delimiter=',')
  for row in data:
    print(row)
    print(row[0])
    print(row[0][1])
