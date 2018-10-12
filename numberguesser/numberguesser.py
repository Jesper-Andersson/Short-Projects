#Purpose: User attempts to guess a randomly generated number within an inputed specific range
from random import randint

run_program = True
tryagain = True

while run_program == True:
	range_start = int(input('Enter your desired minimum number: '))
	range_end = int(input('Enter your desired maximum number: '))
	number = randint(range_start, range_end)

	while tryagain == True:
		print('')
		user_guessed = int(input('Enter your guessed number: '))
		print('')

		if user_guessed == number:
			print('Correct!')
			break
		else:
			print('WRONG!!')
			try_answer = input('Would you like to try again? (Y/N): ')
			if try_answer != ('y' or 'Y'):
				tryagain = False

	print('The answer was: ' + str(number))
	print('')
	replay_answer = input('Would you like to play again (Y/N): ')
	if replay_answer != ('y' or 'Y'):
		break