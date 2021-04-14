import json

numbers = [2, 3, 5, 7, 11, 13]

#writing
filename = 'numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)

#reading
filename = 'numbers.json'
with open(filename) as f:
	numbers = json.load(f)
print(numbers)