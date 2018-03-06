import random

def hangman():
	lines = open('hangman.txt', 'r').read().splitlines()
	word = random.choice(lines).lower()
	guess_word = ['_' for x in range(len(word))]
	guessed_letters = []
	print(' '.join(guess_word))
	counter = 7
	again = None
	

	while True:
		letter = input('Guess a letter, you have {} {} left: '.format(counter, 'try' if counter < 2 else 'tries' )).lower()
		
		while type(letter) != str or len(letter) > 1:
			letter = input('Not a letter, try again: ')
		if letter in word:
			if letter in guessed_letters:
				print('Already guessed')
				counter -= 1
			else:
				for i, x in enumerate(word):
					if x == letter:
						guess_word[i] = letter
				guessed_letters.append(letter)
		else:
			if letter in guessed_letters:
				print('Already guessed')
				counter -= 1
			else:
				guessed_letters.append(letter)
				counter -= 1

		if '_' not in guess_word:
			again = input('You won! Do you want to play again? ')
			

		if counter == 0:
			again = input('You lose. The word was {}. Do you want to play again?'.format(word))
			
		if again:
			if again == 'y' or again == 'yes':
				hangman()
				break
			elif again == 'n' or again == 'no':
				break
			else:
				print('Not yes/y or no/n, ending game')
				break

		print(' '.join(guess_word))


	
	












