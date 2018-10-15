# #list of names
# names = ["Jantje", "Keesje", "Pietje"]
# snacks = []

# index = 0
# #forloop print names and length names
# for name in names:
# 	snack = snacks.append(input(f"{name}, what is your favorite snack? "))
# 	name_length = len(name)
# 	print(f"The length of your name is {str(name_length)} characters.")

# for name in names:
# 	print(f"{name} your favorite snack is {snacks[index]}.")
# 	index = index + 1


# movie = {
# 	"title" : "Deadpool",
# 	"releaseyaer" : 2016,
# 	"duration" : 108,
# 	"director" : "Tim Miller"
# }



#list of names
names = {
	"Jantje": " ", 
	"Keesje": " ",
	"Pietje": " " 
	}

#forloop print names and length names
for name, snack in names.items():
	names[name] = input(f"{name}, what is your favorite snack? ")
	name_length = len(name)
	print(f"The length of your name is {str(name_length)} characters.")

for name, snack in names.items():
	print(f"{name} your favorite snack is {snack}.")