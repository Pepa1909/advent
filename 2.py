soubor = open("advent\\2.txt", encoding="utf-8").read().splitlines()
forward = 0
depth = 0
for n in soubor:
    if n[0] == "f":
        forward += int(n[-1])
    elif n[0] == "d":
        depth += int(n[-1])
    else:
        depth -= int(n[-1])
print(depth*forward)
    