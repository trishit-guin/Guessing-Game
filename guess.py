import random

number = random.randint(1, 10)

name = input("What's your name?")
print('Hello ' + name + '\n')
print('I am choosing a number between 1 and 10: \nYou have to guess the correct number in 3 tries.')
number_of_guesses = 0
choice = 'yes'
while choice in 'yesYES':
	while number_of_guesses < 3:
		guess = int(input('\nEnter your guess'))
		number_of_guesses += 1
		if guess < number:
			print('Your guess is too small\nTry a bigger number')
		if guess > number:
			print('Your guess is too big\nTry a smaller number')
		if guess == number:
			break
	if guess == number:
		if number_of_guesses == 1:
			print('Excellent!\nYou guessed the number in first try. ')
		elif number_of_guesses == 2:
			print('You guessed the number in second try. ')
		else:
			print('You guessed the number in third try')
	else:
		print('\nYou couldn\'t guess the number\tThe number was: ', number)
		print('Better luck next time! ')
	choice = input('\nDo you want to play again: Yes/No')
	if choice in 'yesYES':
		number_of_guesses = 0
		number = random.randint(1, 10)
