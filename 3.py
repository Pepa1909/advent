soubor =open("advent\\3.txt" ,encoding="utf-8").read().splitlines()
N = len(soubor[0])
gamma = ""
epsilon = ""

for n in range(N):
    pocet1 = 0
    pocet0 = 0
    for line in soubor:
        if line[n] == "1":
            pocet1 += 1 
        else:
            pocet0 += 1
    if pocet1 > pocet0:
        gamma += "1"
    else:
        gamma += "0"
    if pocet1 < pocet0:
        epsilon += "1"
    else:
        epsilon+="0"
gamma = int(gamma, 2)
epsilon = int(epsilon,2)
print(gamma* epsilon)
