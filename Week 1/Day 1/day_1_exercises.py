def is_string(s):
	return type(s) == str

def is_only_string(s):
	return type(s) == str and ' ' in s and any(x.isdigit() for x in s)

def is_alphanumeric(s):
	return len(s) > 0 and type(s) == str and s.isalnum()

def is_array_or_tuple(x):
	return type(x) == list or type(x) == tuple

def are_same_type(arr):
	type_to_check = type(arr[0])
	for x in arr:
		if type(x) != type_to_check:
			return False
	return True



def longest_string(s1, s2):
	non_duplicates = []
	for x in s1 + s2:
		if x not in non_duplicates:
			non_duplicates.append(x)
	return ''.join(sorted(non_duplicates))

def convert(n):
	return [int(x) for x in sorted(list(str(n)), reverse=True)]

def count_repetition(arr):
	dic = {}
	for x in arr:
		if x not in dic:
			dic[x] = 1
		else:
			dic[x] += 1
	return dic

def is_caught(s):
	return s.index('m') - s.index('C') < 4

def split_the_bill(group):
	total = 0
	for amount in group.values():
		total += amount
	average = total/len(group)
	return {x:int(average - group[x]) for x in group}

def exp_recursive(b, e, counter=1):
	counter *= b
	if e == 1:
		return counter
	else:
		return exp_recursive(b, e-1, counter)

def zero_sum(arr):
	output_list = []
	for x in arr[:]:
		for y in arr:
			if x + y == 0 and [arr.index(y), arr.index(x)] not in output_list:
				output_list.append([arr.index(x), arr.index(y)])
	return output_list

#sentence = input('Enter a sentence: ')

def count_upper_lower(s):
	lower, upper = 0, 0
	for x in s:
		if x.isupper():
			upper += 1
		elif x.islower():
			lower += 1
	return 'UPPER {} LOWER {}'.format(upper, lower)

#print(count_upper_lower(sentence))

def new_dict(arr):
	dic = {}
	for x in arr[::-1]:
		dic = {x:dic}
	return dic

def gen_dicitionary():
	return {x:x**2 for x in range(1,21)}

def print_dictionary():
	for x in gen_dicitionary().values():
		print(x)

from itertools import permutations

def permute(arr):
	output_list = []
	for x in permutations(arr):
		output_list.append(x)
	return output_list

def write_number(n):
	output_string = ''
	dic = {0:['zero',''],1:['teen','one'],2:['twenty','two'],3:['thirty','three'],4:['forty','four'],5:['fifty','five'],6:['sixty','six'],7:['seventy','seven'],8:['eighty','eight'],9:['ninety','nine']}
	special_dic = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
	if n in special_dic:
		return special_dic[n]
	string_number = str(n)
	num_length = len(string_number)
	if num_length == 1:
		return dic[n][1]
	for i, x in enumerate(string_number):
		output_string += '-' + dic[int(x)][i]
	return output_string[1:] if n % 10 != 0 else output_string[1:-1]
#cuts off the hyphen if the last digit is a zero
print(write_number(17))

