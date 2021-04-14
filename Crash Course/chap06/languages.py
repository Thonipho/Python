favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

#extracting information
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#accomadating information that is not there
language2 = favorite_languages.get('pompo', 'No point value-assigned')
print(language2)

#looping through a dictionary
for key, value in favorite_languages.items():
	print(f"Key: {key.title()} Value: {value.title()}")

#looping for keys only
for key in favorite_languages.keys():
	print(f"Key: {key.title()}")

#looping for values
for value in favorite_languages.values():
	print(f"Values: {value.title()}")

#looping through in a particular order
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

#accessing values using set
for language in set(favorite_languages.values()):
	print(language.title())

