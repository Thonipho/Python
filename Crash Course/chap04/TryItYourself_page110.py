#4-3
for value in range(21):
	print(value)

#4-4	
numbers = list(range(1000000))
for number in numbers:
	print(number)

#4-5
digits = list(range(1000000))
print(min(digits))
print(max(digits))
print(sum(digits))

#4-6
odd_numbers = list(range(1, 20, 3))
print(odd_numbers)

#4-7
multiples = [value*3 for value in range(1, 11)]
print(multiples)

#4-8 & 4-9
cubes = [value**3 for value in range(1, 11)]
print(cubes)



