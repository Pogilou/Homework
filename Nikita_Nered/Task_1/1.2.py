def number_of_characters (string):

    new_string = []
    string = string.lower()
    output = {}

    for item in string:
        if item not in new_string:
            new_string.append(item)

    for item in new_string:
        number = 0
        for i in string:
            if item == i:
                number += 1
        output[item] = number

    return (output)

print(number_of_characters('Oh, it is python'))
