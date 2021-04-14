#3-4
guests = ['mother', 'father', 'brother']
for guest in guests:
	print(f"Hi {guest.title()}, you have been invited")

#3-5
print("Brother cant make it")
del guests[2]
guests.insert(2, 'sister')
for guest in guests:
	print(f"Hi {guest.title()}, you have been invited")

#3-6
print("Cousin,Aunt and Uncle will be joining")
guests.insert(0, 'aunt')
guests.insert(2, 'uncle')
guests.append('cousin')
for guest in guests:
	print(f"Hi {guest.title()}, you have been invited")

#3-7
print("Only 2 people can be invited")
guest1 = guests.pop()
print(f"Sorry {guest1.title()} you have not been invited")
guest2 = guests.pop()
print(f"Sorry {guest2.title()} you have not been invited")
guest3 = guests.pop()
print(f"Sorry {guest3.title()} you have not been invited")
guest4 = guests.pop()
print(f"Sorry {guest4.title()} you have not been invited")

for guest in guests:
	print(f"{guest.title()} you are still invited")

del guests[0:2]
print(f"{guests}")