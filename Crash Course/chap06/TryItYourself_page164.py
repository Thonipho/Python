#6-4
glossary = {'earth': 'the world we live in', 'wicked':'evil intentions', 'deny':'not agreeing ',
 'parked':'being stationary in a designated area'}
glossary['educated'] = 'having education'
glossary['happy'] = 'opposite of sad'
for key, value in glossary.items():
	print(f"{key.title()}: \n{value.title()}\n")

#6-5
rivers = {'nile':'egypt', 'vaal':'mzansi', 'amazon':'brazil'}
for key, value in rivers.items():
	print(f"The {key.title()} runs through {value.title()}")

#6-6
people = ['jen', 'sarah', 'edward', 'phil','john', 'edd']
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

if people in favorite_languages.keys():
	print{f"Thank you for taking poll"}

else:
	print("Please take the poll")