#10-4
filename = 'data/guests.txt'

with open(filename, 'w') as file_object:

	while True:	
		name = input("Enter your name: ")
		if name == 'quit':
			break
		else:
			file_object.write(f"{name} has been here\n")