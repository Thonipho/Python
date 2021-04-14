from random import choice

questions = ["why do we need nice cars?: ", "why do we need to relieve?: "]

question = choice(questions)
awnser = input(question).strip().lower()

while awnser != "just because":
	awnser= input("why?: ")


