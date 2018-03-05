class Ingredient():
	def __init__(self, name, cost):
		self.name = name
		self.cost = cost
		

class Dish():
	def __init__(self, name, price, ingredients):
		self.name = name
		self.price = price
		self.ingredients = ingredients

	def cost(self):	
		ing_cost = 0
		for x in self.ingredients:
			ing_cost += x.cost
		return 10 + ing_cost

	def profit(self):
		return self.price - self.cost()
		

class Restaurant():
	def __init__(self):
		self.dishes = []
		self.customers = {}

	def order_dish(self, dish):
		self.dishes.append(dish)
		print('Order #{}: {}'.format(self.dishes.index(dish), dish.name))

	def order_dish_customer(self, dish, customer):
		self.dishes.append(dish)
		if customer['name'] not in self.customers:
			self.customers[customer['name']] = [dish]
		else:
			self.customers[customer['name']].append(dish)


	def print_check(self):
		total = 0
		for i, x in enumerate(self.dishes):
			total += x.price
			print('Order #{}: {} - {}'.format(i, x.name, x.price))
		print('Total {}'.format(total))

	def print_check_customer(self, customer):
		try:
			tot = 0
			print('Customer: {}'.format(customer['name']))
			for i, dish in enumerate(self.customers[customer['name']]):
				print('Order #{}: {} - {}.00.-'.format(i + 1, dish.name, dish.price))
				tot += dish.price
			print('Total: {}'.format(tot))
		except KeyError:
			print('{} has no orders!'.format(customer['name']))

	def total_profit(self):
		tot = 0
		for dish in self.dishes:
			tot += (dish.price - dish.cost())
		return tot

	def profit_customer(self, customer):
		profit = 0
		for dish in self.customers[customer['name']]:
			profit += (dish.price - dish.cost())
		return profit





		


