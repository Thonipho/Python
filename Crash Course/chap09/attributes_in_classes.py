class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

#setting default value
class Car:
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

    #modifying an attribute using a method
	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value."""
		self.odometer_reading = mileage
		print(f"This car has {self.odometer_reading} miles on it.")

    #incrementing an attributes value through a method
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles 
		print(f"This car has {self.odometer_reading } miles on it.")

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.increment_odometer(100)
my_used_car.update_odometer(23500)

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)


#modifying attributes
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

