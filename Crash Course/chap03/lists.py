bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[1])
#user square brackets and a number to choose a specific item in the list

motorcycles = ['honda', 'yamaha', 'bmw']
motorcycles[0]= 'ducatti'
print(f"{motorcycles}")
#this is how you change an item in the list

print(f"{motorcycles}")
#adding items to a list
motorcycles.append('suzuki')
print(f"{motorcycles}")

#inserting items to a list
motorcycles.insert(0, 'harley')
print(f"{motorcycles}")

#deleting items in a list
del motorcycles[0]
print(f"{motorcycles}")

#extract from list 
first_owned= motorcycles.pop(2)
print(f" First owned motorcycle was a {first_owned}")

#removing an item from the list
motorcycles.remove('ducatti')
print(f"{motorcycles}")

#sorting items in a list
motorcycles.sort()
print(motorcycles)

#sorting items in a list in reverse order
motorcycles.sort(reverse=True)
print(motorcycles)

#finding length of the list
print(len(bicycles))

#selecting a range
players = ['charles', 'martina', 'micheal']
print(players[0:2])



