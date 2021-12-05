import csv
with open("2.csv", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter = " ")
    l_cisla = []
    l_kam = []
    vyska = 0
    dopredu = 0
    for r in reader:
        # l_kam.append(r[0])
        # l_cisla.append(int(r[-1]))
        if r[0]=="forward":
            dopredu+= int(r[-1])
        if r[0]=="up":
            vyska -= int(r[-1])
        if r[0] == "down":
            vyska += int(r[-1])
    print(dopredu*vyska)
    