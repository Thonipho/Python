#7-1
rental = input("What car would you like to rent?")
print(f"Let me see if i can find you a {rental}")

#7-2
seating = input("How many are you in your dinner group")
seating = int(seating)
if seating > 8:
	print("You will have to wait")
else:
	print("Your table is ready")

#7-3
number = input("Enter a number")
number = int(number)
if number % 10 == 0:
	print(f"{number} is a multiple of 10")
else:
	print(f"{number} is not a multiple of 10")