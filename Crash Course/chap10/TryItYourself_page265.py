#10-3
filename = 'data/tryityurself_page265.txt'
name = input("Enter your name")
with open(filename, 'w') as file_object:
	file_object.write(name)

#10-4
filename = 'data/guests.txt'
name = input("Enter your name")
with open(filename, 'w') as file_object:
	while True:	
	if name == 'quite':
		break
	else:
		file_object.write(f"{name} has been here\n")
	

#10-5
