

user_input = int(input("Enter a whole number to find out if the number is prime: "))
prime = True

for number in range(2,user_input):
	if user_input % number == 0:
		prime = False

if prime == True:
	print(f"{user_input} is a prime number.")
else:
	print(f"{user_input} is not a prime number.")