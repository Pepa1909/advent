import csv
with open("3.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(len(row))