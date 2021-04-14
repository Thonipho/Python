#get email address
email = input("what is your email")

#slice username
username = email[:email.index("@")]

#slice domain
domain = email[email.index("@")+1:]

#create output
output = "Your username is {} and your domain is {}"
string = output.format(username, domain)

#print output
print(string)