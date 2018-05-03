

user_input = int(input("Enter a whole number to find out if the number is prime: "))
prime = 0

if user_input == 2:
	prime = True
elif user_input == 5:
	prime = True
elif user_input == 7:
	prime = True
elif user_input % 2 == 0:
	prime = False
elif user_input % 3 == 0:
	prime = False
else:
	prime = True

if prime == True:
	print(f"{user_input} is prime.")
else:
	print(f"{user_input} is not prime.")