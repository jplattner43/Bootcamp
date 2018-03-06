def even_numbers(arr):
	return list(filter(lambda x: x % 2 == 0, arr))

def square_elements(arr):
	return list(map(lambda x: x**2, arr))

def squared_even_numbers(arr):
	return square_elements(even_numbers(arr))

def find_certain_numbers_loop(mi, ma):
	output = []
	for x in range(mi, ma + 1):
		if x % 7 == 0 and x % 5 != 0:
			output.append(x)
	return output

def find_certain_numbers_filter(mi, ma):
	return list(filter(lambda x: x % 7 == 0 and x % 5 != 0, range(mi, ma + 1)))

def compute_totals(orders):
	return list(map(lambda x: (x['id'], x['quantity'] * x['price_per_item'] + 10 if x['quantity'] * x['price_per_item'] < 101 else x['quantity'] * x['price_per_item']), orders))

def square_dicitionary(n):
	return {x:x**2 for x in range(1, n + 1)}

def list_comp():
	a = [x**2 for x in range(1, 21)]
	return a[-5:]

def print_style():
	return ''.join([str(x) if x % 2 == 0 else '_' for x in range(1, 11)])

def bmi():
	print("Let's calculate your BMI (kg/m^2) ")
	w = input('Input your weight in kg: ')
	h = input('Input your height in cm: ')
	bmi = float(w)/((float(h)/100)**2)
	if bmi < 18.5:
		s = 'underweight'
	elif 18.5 < bmi < 25:
		s = 'normal weight'
	else:
		s = 'overweight'
	print('Your BMI is {} and you are {}'.format(bmi, s))

# Shooping list app

def shopping_list():
	items = []

	def help_menu():
		print(r'Press "a" to add items to the shopping list. Press "s" to show the items in the list, "r" to remove and "q" to quit the app')
	print("Press 'h' for help menu ")

	def add_item():
		item = input('What do you want to add (with optional index after a space)? ')
		if item[-2] == ' ':
			items.insert(int(item[-1]), item[:-2])
		else:
			items.append(item)

	def remove_item():
		item = input('What do you want to remove? ')
		try:
			items.remove(item)
		except ValueError:
			print('No such item!')

	def show_items():
		if items == []:
			print('There are no items on the list!')
		for i, x in enumerate(items):
			print('{}: {}'.format(i + 1, x))

	while True:
		letter = input('What do you want to do? ')
		if letter == 's':
			show_items()
		elif letter == 'a':
			add_item()
		elif letter == 'r':
			remove_item()
		elif letter == 'h':
			help_menu()
		elif letter == 'q':
			break
		else:
			print('Try again ')


# Number guess game

from random import randint

def number_game():
	the_number = randint(1, 10)
	counter = 1

	def play_again():
		number_game()

	print('I am thinking of a number from 1-10. Can you find it? You have 5 tries.')
	while True:
		n = input('Guess what it is: ')
		while type(n) != int:
			n = input('Not an integer, try again: ')
		if n == the_number:
			print('Congrats, you guessed it in {} {}!'.format(counter, 'try' if counter == 1 else 'tries'))
			again = input('Do you want to play again? ')
			if again == 'yes' or again == 'y':
				play_again()
				break
			elif again == 'no' or again == 'n':
				break
		elif the_number < n:
			print("Nope. It's lower than that. Try again.")
		elif the_number > n:
			print("Nope. It's higher than that. Try again.")

		if counter == 5:
			print('You lose.')
			break
		counter += 1






