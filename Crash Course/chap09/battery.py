class battery():
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		self.battery_size = 75
		batteryinfo=f"This car has a {self.battery_size}-kWh battery."
		return batteryinfo

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")
		