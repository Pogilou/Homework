def get_digits(num):
    tuple_of_integers = []
    for i in str(num):
        tuple_of_integers.append(int(i))
    tuple_of_integers = tuple(tuple_of_integers)
    return tuple_of_integers

print (get_digits(87178291199))



