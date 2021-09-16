def my_list (input_list):

    set_list = list(set(input_list))
    set_list.sort()
    return set_list

print(my_list (['red', 'white', 'black', 'red', 'green', 'black']))