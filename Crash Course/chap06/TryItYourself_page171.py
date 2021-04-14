#6-7
people = {
 '1':{
'first': 'T',
'last': 'Mav',
'location': 'venda'
},
'2':{
'first': 'curtis',
'last': 'jones',
'location': 'liverpool'
},
'3':{
'first': 'kevin',
'last': 'debruyne',
'location': 'manchester'
}
}

#extracting info
for user_name, user_info in people.items():
	full_name = f"{user_info['first']} {user_info['last']}"
	location = f"{user_info['location']}"
	print(f"{full_name}")
	print(f"{location}\n")

#6-8
pets = {'1':{'kind':'dog','owner':'thabo'}, '2' :{'kind':'cat','owner':'mark'}}
for number, pet in pets.items():
	petinfo = f"{pet['kind']}"
	petowner = f"{pet['owner']}"
	print(f"{petinfo.title()}")
	print(f"{petowner}\n")

#6-9
places ={'thabo':{'1':'jozi','2':'east','3':'kapa'}, 'mav' :{'1':'durban','2':'kimberley','3':'mams'}}
for name,place in places.items():
	place1=f"{place['1']}"
	place2 = f"{place['2']}"
	place3= f"{place['3']}"
	print(f"{name}")
	print(f"{place1} {place2} {place3}\n")\

	