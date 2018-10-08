import json

with open("movies.json") as f:
	json_data = json.load(f)

year_input = int(input("Give a year: "))

#basis exercise
for movie in json_data:
	year = movie["year"]
	title = movie["title"]
	if year_input == year:
		print(f"{title} is from year {year}")

print("1 for movies longer than a certain duration")
print("2 for movies where the director is also an actor")
print("3 for movies that here directed by a specific director")
print("4 for showing the genres of a movie")
print("5 for showing the movies that got a given genre")
print("6 for showing all inforamtion about a movie")
question = input("Type your answer: ")

if question == "1":
	duration_input = int(input("type a duration in minutes: "))
	for movie in json_data:
		duration = int(movie["duration"])
		title = movie["title"]
		if duration >= duration_input:
			print(f"The duration of {title} the same or longer than {duration_input} minutes")
		else:
			print("There are no movies with this duration (or longer)")

elif question == "2":
	for movie in json_data:
		director = movie["director"]
		actors = movie["actors"]
		title = movie["title"]
		if director in actors: 
			print(f"{director} is the director and an actor in {title}")

elif question == "3":
	director_input = input("Type a director: ").title()
	for movie in json_data:
		director = movie["director"]
		title = movie["title"]
		if director == director_input:
			print(f"{title} is also directed by {director}")

elif question == "4":
	title_input = input("Type a title of a movie ")
	for movie in json_data:
		title = movie["title"]
		genres = movie["genres"]
		if title == title_input:
			print(f"The genres of {title} are:")
			for genre in genres:
				print("      " + genre)

elif question == "5":
	genre_input = input("Type a genre: ")
	for movie in json_data: 
		title = movie["title"]
		genres = movie["genres"]
		if genre_input in genres:
			print(f"The movie {title} got genre {genre_input}")

elif question == "6":
	title_input = input("Type a title of a movie: ")
	for movie in json_data: 
		title = movie["title"]
		genres = movie["genres"]
		director = movie["director"]
		actors = movie["actors"]
		duration = int(movie["duration"])
		if title_input in title:
			print(f"title: {title}")
			print(f"director: {director}")
			print(f"duration: {duration} minutes")
			print(f"actors: ")
			for actor in actors:
				print("      " + actor) 
			print(f"The genres of {title} are: ")
			for genre in genres:
				print("      " + genre)

else: 
	print("That was not an option")