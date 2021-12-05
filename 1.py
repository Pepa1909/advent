import csv

with open("1.txt", encoding="utf-8") as f:
    vyssi = 0
    l =[]
    for r in f:
        l.append(int(r))
        if len(l) > 1:
            if l[-1] > l[-2]:
                vyssi+=1
    print(vyssi)
