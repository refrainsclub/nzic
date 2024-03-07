teas = {"G": 0, "C": 0, "E": 0, "P": 0, "L": 0, "S": 0}

line = input()
while line != "D":
    flavour, n = line.split()
    teas[flavour] += int(n)
    line = input()

print(" ".join(map(str, teas.values())))
