#open the csv file
footballers = open("footballers.csv")

newfile = open("footballers.txt", "w")

#first exercise
for player in footballers:
	player = player.strip().split(",")
	#print(player)
	names = player[0]
	clubs = player[1]
	price = player[2]
	newfile.write(names + " is transfered to " + clubs + " for " + price + "000000" + " milion dollars.") 
	print(names + " is transfered to " + clubs + " for " + price + " milion dollars.")

newplayername = input("Write down another player: ")
newplayerclub = input("To which club is he or she transfered? ")
newplayerprice = input("For how much money is he transfered in millions? (add six zeros) ")

newplayerrow = "\n" + newplayername + "," + newplayerclub + "," + newplayerprice + "\n"

footballers.close()

footballers = open("footballers.csv", "a")

footballers.write(newplayerrow)


newfile.close()
footballers.close()
