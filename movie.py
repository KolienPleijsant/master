#create dictionaries
movie = {
	"title" : "Deadpool",
	"releaseyaer" : 2016,
	"duration" : 108,
	"director" : "Tim Miller"
}

#basis exercise
for key, val in movie.items():
	print(f"{key}: {val}")

#extend exercise
#add actors in the dictionary
movie["actors"] = ["Ryan Reynolds", "Karon Soni", "Ed Skrein"]

#for loop to print the values
for key, val in movie.items():
	#if duration or actors are key print something else
	if key == "duration":
		print(f"{key}: {val} minutes")
	elif key == "actors":
		actors = ", ".join(val)
		print("actors: " + actors)
	else:	
		print(f"{key}: {val}")