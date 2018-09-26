#asking for the names
name_1 = input("What is your name?")
name_2 = input("What is your lovers name?")

#make the names all lowercase
name_1 = name_1.lower()
name_2 = name_2.lower()

#delete spaces around the names
name_1 = name_1.strip()
name_2 = name_2.strip()

#the comments below is the code for the basic assignment
#if name_1 == name_2:
#	print("You are in love with yourself")
#elif name_1 > name_2:
#	print("It's a match!")
#else:
#	print("You are not a match, go dating again")

#counting the characters in both names
count_name_1 = len(name_1)
count_name_2 = len(name_2)

#because the difference between the amount of characters of the names can be mines, abs makes it a plus
count_dif = abs(count_name_1 - count_name_2)

#if the difference between the amount of characters is low, the % of the match is higher
if count_dif == 0:
	print("You are a 100% match!")
elif count_dif == 1:
	print("You are a 80% match")
elif count_dif == 2:
	print("You are a 60% match")
elif count_dif == 3:
	print("You are a 40% match")
elif count_dif == 4:
	print("You are a 20% match")
elif count_dif == 5:
	print("You are a 10% match")
else:
	print("You are a 0% match")