#writing
filename = 'data/programming.txt'
with open(filename, 'w') as file_object:
	file_object.write("I love programming.")
	file_object.write("I love creating new games.")

#appending
with open(filename, 'a') as file_object:
	file_object.write("I love programming.")
	file_object.write("I love creating new games.")


