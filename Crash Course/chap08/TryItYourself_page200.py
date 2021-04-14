#8-3
def make_shirt(size,text):
	print(f"Shirt size is: {size} \nShirt text is: {text}")

#8-4
def make_shirt(size = 'large',text = 'i love python'):
	print(f"Shirt size is: {size} \nShirt text is: {text}")
make_shirt(text = 'life is good')

#8-5
def make_cities(city, country = 'South Africa'):
	print(f"{city} is in {country}")
make_cities('kapa')
make_cities('durban')
make_cities('rio', country = 'Brazil')