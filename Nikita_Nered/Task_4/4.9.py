import string

def pars_string(strings):
    characters_in_2_lines = []
    characters_in_all_lines = []
    all_unique_symbols = set()
    not_used_symbols = set()

    for elem in strings: #1
        for word in elem:
            proverka = 0
            for elem1 in strings:
                if word in elem1:
                    proverka += 1
            if proverka == len(strings):
                characters_in_all_lines.append(word)
    characters_in_all_lines = set(characters_in_all_lines)
    print(characters_in_all_lines)


    for elem in strings: #2
        for letter in elem:
            all_unique_symbols.add(letter)
    print(all_unique_symbols)


    for elem in strings: #3
        for word in elem:
            proverka = 0
            for elem1 in strings:
                if word in elem1:
                    proverka += 1
            if proverka >= 2:
                characters_in_2_lines.append(word)
    characters_in_2_lines = set(characters_in_2_lines)
    print(characters_in_2_lines)



    for elem in string.ascii_lowercase:  # 4
        if elem not in all_unique_symbols:
            not_used_symbols.add(elem)
    print(not_used_symbols)




pars_string(["hello", "world", "python", ])