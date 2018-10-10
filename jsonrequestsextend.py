#import requests and json
import requests
import json

#ask for a title of a wikipediapage, stip it and replace the spaces with _
user_input = input("Type in the title of a Wikipedia article: ").strip().replace(" ", "_")
#make a variable for different languages
language = ["en", "es", "nl"]
languages = ["English", "Español", "Nederlands"]

#set index to 0
index = 0

#for every language do the following code:
for item in language: 
	#make the url with the different languages
	url = f"https://{item}.wikipedia.org/api/rest_v1/page/summary/{user_input}"

	req = requests.get(url)
	#check if the status code is 200
	status = req.status_code
	if status != 200:
		print("ERROR")
	 	#exit()

	#load json
	data = json.loads(req.text)
	print(f'\n{languages[index]}:')

	#check if there is a title and print the title
	if "title" in data:
		title = data["title"]
		print(f'Title: {title}')

	#check if there is a description and print it
	if "description" in data:
		description = data["description"]
		print(f'Description: {description}')

	#check if there is a extract and print it
	if "extract" in data:
		extract = data["extract"]
		print(f'Extract: {extract}')
	index = index + 1