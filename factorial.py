

user_number = int(input("Enter a whole number to found out the factorial for that number: "))
total = 1

while user_number > 0:
	total = user_number * total
	user_number = user_number - 1
	
print(total)