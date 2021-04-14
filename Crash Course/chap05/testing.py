while True:
	age = input("Please enter your age to check price or enter 0 to quit")
	age = int(age)
	if age == 0:
		break
	if age < 3:
		print("Ticket is free")
	elif age > 3 and age < 12:
		print("Ticket is 10$")
	else:
		print("Ticket is 15$") 