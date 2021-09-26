def call_once(func):
    first_call_result = []
    def wrapper(*args):
        try:
            print(first_call_result[-1])
            return first_call_result[-1]
        except:
            first_call_result.append(func(*args))
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


sum_of_numbers (1, 2)
sum_of_numbers (2, 3)
sum_of_numbers (3, 3)
