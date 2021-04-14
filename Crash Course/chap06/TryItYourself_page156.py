#6-1
person = {'first_name': 'John', 'last_name':'Wick', 'age':'20', 'city':'kapa'}
for key, value in person.items():
	print(f"{key} : {value}")

#6-2
numbers = {'john': '1', 'wick':'2', 'dani':'3', 'lesego':'4'}
for key, value in numbers.items():
	print(f"{key} : {value}")

#6-3
glossary = {'earth': 'the world we live in', 'wicked':'evil intentions', 'deny':'not agreeing ',
 'parked':'being stationary in a designated area'}
for key, value in glossary.items():
	print(f"{key.title()}: \n{value.title()}\n")

