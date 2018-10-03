#list of names
friends = [
	["Jantje", " "],
	["Keesje", " "],
	["Pietje", " "]
]

#forloop for the lenght in names
for friend in friends:
	length_name = len(friend[0])
	print(friend[0] + " is " +  str(length_name) + " characters long.")
	
#add the snacks to the list
for friend in friends:
	friend[1] = input("What is your favorite snack " + friend[0] + "?")

#print all the names and snacks
for friend in friends:
	print(friend[0] + " your favorite snack is " + friend[1])
