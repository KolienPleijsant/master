#make a list with wrong words and make an empty list
wrong = ["internet", "computer", "laptop", "apple", "mac", "windows", "ios", "master"]
words = []

#Ask for a sentence, put it in the list "words" and split it at the spaces.
sentence = input("Enter your sentence here. ")
words = sentence.split(" ")

#creating a forloop to make sure the words are checked if they are in the wronglist. 
#the ifstatment in the other ifstatment is to change the words in the sentence from the wronglist in other words
index = 0
for word in words:
	#print(words[index])
	if words[index] in wrong:
		#print("error")
		if words[index] == "internet":
			words[index] = "papier"
		elif words[index] == "computer":
			words[index] = "printer"
		elif words[index] == "laptop":
			words[index] = "desktop"
		elif words[index] == "apple":
			words[index] = "peer"
		elif words[index] == "mac":
			words[index] = "windows"
		elif words[index] == "windows":
			words[index] = "mac"
		elif words[index] == "ios":
			words[index] = "windowsXP"
		elif words[index] == "master":
			words[index] = "kleuterklas"
		else:
			words[index] = words[index]
	else:
		#print("no worries")
		" "
	index = index + 1

#make it a sentence again
words = " ".join(words)

#print the new sentence
print("the new sentence is: " + words)