#importeren requests
import requests

#ask for a url
u = input("Copy past an URL: ").strip()

#request the website for the given url
r = requests.get(u)

#check if the status code is 200, otherwhise exit the program
status = r.status_code
if status != 200:
	print("ERROR")
	exit()
else:
	print("Het werkt")

#put the headers in a variable
h = r.headers

#print the keys and values of the headers
for key, value in h.items(): 
	print(f"{key} : {value}")

#put the text of the url in a variable
text = r.text

#set index to 0
index = 0

#print only the first 10 lines
while index <= 10:
	line = text.splitlines()[index]
	print(line)
	index = index + 1