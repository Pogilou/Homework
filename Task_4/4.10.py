def generate_squares(number):
    quadratoa_dictionary = {}
    for i in range(number):
        quadratoa_dictionary[i+1] = i+1 ** 2
    return quadratoa_dictionary

print(generate_squares(10))