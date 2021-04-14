#4-10
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

print("Here are the middle three players on my team:")
for player in players[1:4]:
	print(player.title())

print("Here are the last three players on my team:")
for player in players[2:]:
	print(player.title())

#4-11
my_pizzas = ['cheese', 'mince', 'bacon']
friend_pizzas = ['cheese', 'mince', 'bacon']
my_pizzas.append('peppa')
friend_pizzas.append('moazzarella')
for pizza in my_pizzas:
	print(f"My pizzas are {pizza}")
for pizza in friend_pizzas:
	print(f"My friends pizzas are {pizza}")
