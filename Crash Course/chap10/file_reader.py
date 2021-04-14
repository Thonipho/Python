#method 1
with open('data/pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents.strip()) 

#method 2
file = 'data/pi_digits.txt'
with open(file) as file_object:
	contents = file_object.read()
print(contents.strip()) 

#read line by line
with open(file) as file_object:
	for line in file_object:
		print(line.strip()) 

#Making a List of Lines from a File
with open(file) as file_object:
	lines = file_object.readlines()
	for line in file_object:
		print(line.strip()) 

#Working with a File’s Contents
with open(file) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
print(f"{pi_string}\n")
print(len(pi_string))