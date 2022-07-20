import random

num = random.randint(1,10)
guess = None

while guess != num:
	guess = input('Enter a number between 1 and 10:')
	guess = int(guess)
	if guess == num:
		print('Correct!')
		break
	else:
		print('Incorrect!')
