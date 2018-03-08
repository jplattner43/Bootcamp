# 1. Race

class Car:
	def __init__(self, color, tank_size, num_laps, len_lap):
		self.color = color
		self.tank_size = tank_size
		self.num_laps = num_laps
		self.len_lap = len_lap

	def any(self, *args, **kwargs):
		pass

	def run_laps(self):
		self.tank_size -= 0.2 * self.len_lap
		return self.tank_size

	def check_pit_stop(self):
		if self.tank_size < 10:
			print('Please refill tank')
		else:
			print('No need to refill')

# 2.Books

class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

	def __str__(self):
		return str('{} by {}'.format(self.title, self.author))

class Bookcase:
	def __init__(self, *books):
		self.book_list = []
		self.book_list.extend(books)

	def create_book(self, title, author):
		self.book_list.append(Book(title, author))

	def __iter__(self):
		return iter(self.book_list)

	def print_books(self):
		for book in self.book_list:
			print('{} by {}'.format(book.title, book.author))


class Quark:
	def __init__(self, ty):
		self.type = ty
		if self.type.lower() == 'up':
			self.charge = 0.666
		elif self.type.lower() == 'down':
			self.charge = -0.333
		else:
			self.charge = 'Unknown charge'

	def symbol(self):
		return 'U' if self.charge == 0.666 else 'D'

	def __str__(self):
		return 'Type: {}; Charge: {}'.format(self.type, self.charge) + '\nSymbol: {}'.format(self.symbol())
		

class Nucleon:
	def __init__(self, ty):
		self.quarks = []
		if ty.lower() == 'proton':
			self.type = 'Proton'
			self.quarks.extend([Quark('up'), Quark('up'), Quark('down')])
		elif ty.lower() == 'neutron':
			self.type = 'Neutron'
			self.quarks.extend([Quark('up'), Quark('down'), Quark('down')])
		else:
			self.type = 'Unknown'
		self.charge = self.get_charge()

	def get_charge(self):
		tot = 0
		for quark in self.quarks:
			tot += quark.charge
		return tot


	def add_quarks(self, *quarks):
		self.quarks.extend(quarks)
		self.charge = self.get_charge()

	def __str__(self):
		return '{}\nThe {} contains {} quarks - {} with {}{}e elementary charge'.format(self.type[0], self.type, len(self.quarks), self.type,'+' if self.charge >= 0 else '', self.charge)

class Atom:
	def __init__(self, name):
		self.name = name
		self.protons = []
		self.neutrons = []
		if self.name.lower() == 'oxygen':
			self.protons.extend(Nucleon('proton') for x in range(8))
			self.neutrons.extend(Nucleon('neutron') for x in range(8))
			self.charge = -2
			self.position = '1 1 1'
		elif self.name.lower() == 'hydrogen':
			self.protons.append(Nucleon('proton'))
			self.charge = 0
			self.position = '2 2 2'
		self.atomic_mass = len(self.protons) + len(self.neutrons)
		self.atomic_number = len(self.protons)

	def __str__(self):
		return ('Symbol: {}\nName: {}\nDescription:\n-Atomic number: {}\n-Atomic mass: {}\n-Position: {}\n-Charge: {}'.format(self.name[0].upper(), self.name, self.atomic_number, self.atomic_mass, self.position, self.charge))




class Molecule:
	def __init__(self, name='Default Molecule'):
		self.name = name
		self.atoms = []
		# should probably have like a dictionary with various molecules and then adjust the properties
		# based on the dictionary values
		if self.name.lower() == 'water':
			self.atoms.extend([Atom('oxygen'), Atom('hydrogen'), Atom('hydrogen')])

	def add_atom(self, atom):
		self.atoms.append(atom)

	def __str__(self):
		print('This is a molecule named {} and it has {} atoms'.format(self.name, len(self.atoms)))
		print('The atoms are:')
		for i, atom in enumerate(self.atoms):
			print(str(i + 1) + ' ' + str(atom))
		return ''

# 4.Inheritance
from math import pi


class Shape:
    def __init__(self, x,y):
      self.center = (x,y)

    def get_area(self):
      # empty shape does not have an area -> return 0
      return 0

class Triangle(Shape):
	def __init__(self, x, y, width, height):
		super().__init__(x, y)
		self.width = width
		self.height = height

	def get_area(self):
		return self.width/2 * self.height

class Rectangle(Triangle):
	def __init__(self, x, y, width, height):
		super().__init__(x, y, width, height)

	def get_area(self):
		return self.width * self.height

class Circle(Shape):
	def __init__(self, x, y, radius):
		super().__init__(x, y)
		self.radius = radius

	def get_area(self):
		return pi * self.radius ** 2

class House:
	def __init__(self, base_shapes, non_paint_surfaces):
		self.base_shapes = base_shapes
		self.non_paint_surfaces = non_paint_surfaces

	def get_paint_area(self):
		whole_area, non_paint_area = 0, 0
		for x in self.base_shapes:
			whole_area += x.get_area()
		for y in self.non_paint_surfaces:
			non_paint_area += y.get_area()
		return whole_area - non_paint_area
		

# 5.Math Quiz

class Questions:
	text = None
	answer = None

class Add(Questions):
	def __init__(self, arg1, arg2):
		self.arg1 = arg1
		self.arg2 = arg2
		self.text = '{} + {} = ? '.format(self.arg1, self.arg2)

	def get_answer(self):
		return self.arg2 + self.arg1

class Multiply(Add):
	def __init__(self, arg1, arg2):
		super().__init__(arg1, arg2)
		self.text = '{} * {} = ? '.format(self.arg1, self.arg2)

	def get_answer(self):
		return self.arg1 * self.arg2

class Divide(Add):
	def __init__(self, arg1, arg2):
		super().__init__(arg1, arg2)
		self.text = '{} / {} = ? '.format(self.arg1, self.arg2)

	def get_answer(self):
		return self.arg1/self.arg2

import random
import timeit

class TheQuiz:
	def __init__(self):
		self.possible_questions = [Divide, Add, Multiply]
		
		self.start = timeit.default_timer()
		self.counter = 0
		for x in range(15):
			a = random.choice(self.possible_questions)(random.randint(1,10), random.randint(1,10))
			s = input(a.text)
			
			if float(s) == float(a.get_answer()):
				print('Correct')
				self.counter += 1
			else:
				print('Wrong, answer is {}'.format(a.get_answer()))
				print(type(a.get_answer()))
		print('You got {} questions right and it took you {} seconds'.format(self.counter,timeit.default_timer() - self.start))

qq = TheQuiz()

# Magic Methods, incomplete

class Account:
	def __init__(self, name, amount):
		self.name = name
		self.amount = amount
		self.transactions = []

	def __str__(self):
		return '{} {} {} CHF'.format(self.name,'have' if '&' in self.name else 'has', self.amount)

	def __len__(self):
		return len(self.transactions)


	def __add__(self, account):
		return Account(self.name + ' & '  + account.name, self.amount + account.amount)

	def __reversed__(self):
		return reverse(self.transactions)














