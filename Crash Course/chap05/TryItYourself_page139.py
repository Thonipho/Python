#5-3
alien_colours = ['green', 'yellow', 'red']
if 'green' in alien_colours:
	print("Player earned 5 points")

#5-4
if 'green' in alien_colours:
	print("Player earned 5 points for shooting alien")
if alien_colours != 'green':
	print("Player earned 10 points")

#5-5
if 'green' in alien_colours:
	print("Player earned 5 points")
elif alien_colours == 'yellow':
	print("Player earned 10 points")
elif alien_colours == 'red':
	print("Player earned 15 points")

#5-6
age = 5
if age <2:
	print("You are a baby")
if age >= 2 and age <4:
	print("You are a toddler")
if age >=4 and age <13:
	print("You are a kid")
if age >=13 and age<20:
	print("You are an adult")
if age >65:
	print("You are an elder")

#5-7
fruits = ['apple', 'banana', 'grape']

for fruit in fruits:
	if fruit in fruits:
		print(f"You really like {fruit}")
	