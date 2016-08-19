def super_sum(*numbers):
	if not len(numbers):
		return 'list empty'
	total_n = 0
	total_l = 0
	for number in numbers:
		if type(number) == list:
			for num in number:
				if type(num) == str:
					return 'invalid data type'
				total_l = total_l + num
		else:
			if type(number) == str:
				return 'invalid data type'
			total_n = total_n + number
		# total += number
	return total_n + total_l
