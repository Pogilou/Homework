
def remember_result(func):
	list_of_results = []
	def wrapper (*args):
		try:
			print("\nLast result: {result}  ".format (result=list_of_results[-1]))
			if args not in list_of_results:
				list_of_results.append(func(*args))
			return list_of_results[-1]
		except IndexError:
			list_of_results.append(func(*args))
			return None

	return wrapper




@remember_result
def sum_list(*args):

	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result

sum_list("s", "b")

sum_list("123", "b")

sum_list("111", "222")

