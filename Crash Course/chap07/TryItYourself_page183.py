#7-4
while true:
	topping = input("Please choose a topping or type quit to exit")
	if topping == 'quit':
		break
	else:
		print(f"{topping} will be added to your toppings")

#7-5
while true:
	age = input("Please enter your age")
	age = int(age)
	if age < 3:
		print("Ticket is free")
	elif age > 3 and age < 12:
		print("Ticket is 10$")
	else:
		print("Ticket is 15$")  

#7-6
while true:
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

#7-7
x=1
while x<1:
	print(x)