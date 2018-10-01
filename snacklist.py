#list of names
names = ["Jantje", "Keesje", "Pietje"]
snacks = []

index = 0
#forloop print names and length names
for name in names:
	snack = input(name + ", what is your favorite snack?")
	snacks.append(snack)
	name_length = len(name)
	print("The length of your name is " + str(name_length) + "characters.")

for name in names:
	print(name + " your favorite snack is " + snacks[index] + ".")
	index = index + 1
