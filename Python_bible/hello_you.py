#ask for name
name = input("What is your name?: ")

# ask for age
age = input("how old are you?: ")

#ask for address 
address = input("where do you live?: ")

#ask for interests
interest = input("what do you enjoy doing?: ")

#create output text
string = "Your name is {} and you are {} years old. You live in {} and you enjoy {}"
output = string.format(name,age,address,interest)

#print output
print(output)