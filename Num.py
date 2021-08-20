from random import randint
num=randint(1,9)
guess=-1
name=input("Hello,What's your name?")


print('Great '+name+' Guess the number between 1 & 10:')
while guess!=num:
	guess=int(input("Guess the Number:"))
	if guess!=num:
		print("OOPS,Wrong guess")

	else:
		print("Congratulations,the number you guessed is correct")
