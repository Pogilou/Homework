dict_1 = {'a': 100, 'd': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}


def combine_dicts(*args):
    dict_combine = {}
    for elem in args:
        for key in elem:
            if key not in dict_combine:
                dict_combine[key] = elem[key]
            else:
                new_elem = dict_combine[key] + elem[key]
                dict_combine[key] = new_elem
    return (dict_combine)


print(combine_dicts(dict_1,dict_2,dict_3))