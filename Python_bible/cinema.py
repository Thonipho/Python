films = {
	'finding dory' : {'age':3, 'seats':5},
	'bourne' : {'age':18, 'seats':5},
	'tarzan' : {'age':15, 'seats':0},
	'ghost busters' : {'age':12, 'seats':5}
}

while True:
	choice = input("Which movie would you like to watch?: ").strip()

	if choice in films:
		age = int(input("How old are you?: ").strip())

		if age >= films[choice]['age']:

			if films[choice]['seats'] > 0:
				films[choice]['seats'] = films[choice]['seats']-1
				print("Enjoy the movie")

			else: 
				print("Tickets are sold out")

		else:
			print("You are too young to watch that movie")
	else:
		print("We dont have that film...")
