#9-4
class restaurent:

	def __init__(self,name,cousintype):
		self.name = name
		self.cousintype = cousintype
		self.servedcustomers = 0
		self.attempts = 0

	def describe(self):
		description = f"{self.name} is a {self.cousintype} type of cousin"
		return description

	def open_restaurant(self):
		message = f"{self.name} is open"
		return message

	def set_number_served(self,served):

		self.servedcustomers = served
		print(f"{self.servedcustomers} customers has been served")

	def increment_served(self,served_added):

		self.servedcustomers += served_added
		print(f"{self.servedcustomers} customers has been served today")

	def increment_login_attempts(self,attempting):

		self.attempts = attempting + 1
		print(f"{self.attempts}")

	def remove_attempts(self, attempted):

		self.attempts = 0
		print(f"{self.attempts}")

describing1 = restaurent("KFC","Fast Food")
describing1.set_number_served(20)
describing1.increment_served(30)
describing1.increment_login_attempts(1)
describing1.remove_attempts(2)