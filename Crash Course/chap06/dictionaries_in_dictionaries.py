#setting a dictionary in a dictionary
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
}
}

#extracting info
for user_name, user_info in users.items():
	print(f"Name:{user_name}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = f"{user_info['location']}"
	print(f"UserName:{user_name}")
	print(f"{full_name}")
	print(f"{location}\n")

#setting a dictionary in a dictionary
vehicles = {
'bmw': {
'sedan': '3 series',
'suv': 'x5m',
'location': 'midrand',
},
'benz': {
'sedan': 'c class',
'suv': 'gle',
'location': 'pitori',
}
}

#extracting info
for brands, vehicle in vehicles.items():
	print(f"Brand:{brands}")
	sedan = f"{vehicle['sedan']}"
	suv = f"{vehicle['suv']}"
	location = f"{vehicle['location']}"
	print(f"Sedan:{sedan}")
	print(f"SUV:{suv}")
	print(f"location:{location}\n")



