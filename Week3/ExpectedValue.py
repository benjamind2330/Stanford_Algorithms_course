

diceRoll = []

for i in range(1, 7):
	for j in range(1, 7):
		diceRoll.append((i, j))


eV = 0.0

for (d1, d2) in diceRoll:
	print(str(d1) + " , " + str(d2) + "\t" + str(d1+d2))
	eV = eV+(d1+d2)*1.0/36.0

print("expected value ", eV)


