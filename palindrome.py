

word = input("Please enter a word to find out whether or not it's a palindrome: ")
letters = list(word)

for index in range(0,len(letters)):
	if letters[0] == letters[-1]:
		print(f"{word} is a palindrome.")


# I'm stuck. I can't figure out where to go from here. Not sure I'm even on the right path.


