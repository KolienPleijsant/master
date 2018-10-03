#first part of the exercise
sentence = input("Type in a sentence: ")
length = len(sentence)
#print(length_sentence)

#calculate the first 25% and last 75%
start = round(length * 0.25)
end = round(length * 0.75)

#print(start)
#print(end)

#print the middle part
print(sentence[start:end])

#second part of the exercise
#split the sentence by at the space
sentencelist = sentence.split(" ")
word_count = len(sentencelist)
#print(word_count)

#calculate the first 25% of the words and last 75%
startword = round(word_count * 0.25)
endword = round(word_count * 0.75)

#print(startword)
#print(endword)
#print(sentencelist[startword:endword])

#change the list to only the middle part
sentencelist = sentencelist[startword:endword]

#tranform the list to a sentence with spaces
sentencelist = " ".join(sentencelist)

#print the sentence
print(sentencelist)