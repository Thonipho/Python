#7-8
sandwich_orders = ['cheese', 'ham', 'egg']
finished_sandwich = []

while sandwich_orders:
	done = sandwich_orders.pop()
	print(f"I made your {done} sandwich")
	finished_sandwich.append(done)
print(f"The following sandwiches were made {finished_sandwich}\n")

#7-9
sandwich_orders = ['cheese', 'ham', 'egg', 'Pastrami', 'Pastrami', 'Pastrami']
finished_sandwich = []
print("Pastrami sandwiches are finished")
while sandwich_orders:
	while 'Pastrami' in sandwich_orders:
		sandwich_orders.remove('Pastrami')
	done = sandwich_orders.pop()
	print(f"I made your {done} sandwich")
	finished_sandwich.append(done)

print(f"The following sandwiches were made {finished_sandwich}\n")

#7-10
info = {}
poll= True
while poll:
	name = input("What is your name:\t")
	vacation = input("If you could visit one place in the world where would it be:\t")
	info[name] = vacation
	quite = input("Is there a next user yes/no?")
	if quite == 'no':
		poll = False
for name, vacation in info.items():
	print(f"{name} would like to visit {vacation}")		
			




