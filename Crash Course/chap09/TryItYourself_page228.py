#9-1
class restaurent:

	def __init__(self,name,cousintype):
		self.name = name
		self.cousintype = cousintype

	def describe(self):
		description = f"{self.name} is a {self.cousintype} type of cousin"
		return description

	def open_restaurant(self):
		message = f"{self.name} is open"
		return message

#9-2
describing1 = restaurent("KFC","Fast Food")
describing2 = restaurent("Steers","Fast Food")
describing3 = restaurent("Debonairs","Fast Food")
print(describing1.describe())
print(describing1.open_restaurant())
print(describing2.describe())
print(describing2.open_restaurant())
print(describing3.describe())
print(describing3.open_restaurant())

#9-3
class user:
	def __init__(self,name,surname,age, nationality):
		self.name = name
		self.surname = surname
		self.age = age
		self.nationality = nationality

	def describe(self):
		description = f"{self.name} {self.surname} is {self.age} years old and he/she is from {self.nationality}"
		return description

	def greeting(self):
		message = f"Hello {self.name}"
		return message

user1 = user("Nelson","Mandela",99,"South Africa")
user2 = user("Jacob","Zuma",80,"South Africa")
print(user1.describe())
print(user1.greeting())
print(user2.describe())
print(user2.greeting())


