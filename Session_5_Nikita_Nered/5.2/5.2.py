import string

def most_common_words(filepath, number_of_words=3):

    file = open(filepath, 'r')
    file_lines = file.read()
    file.close()

    words = file_lines.split()

    for num, i in enumerate(words):
        if i[-1] not in string.ascii_lowercase:
            words[num] = i[:-1]

    unique_words = set(words)

    number_of_repetitions = {}

    for word in unique_words:
        repetitions = 0
        for item in words:
            if item == word:
                repetitions += 1
            number_of_repetitions[word] = repetitions

    most_popular_words = []

    list_items = list(number_of_repetitions.items())
    list_items.sort(key=lambda i: i[1])
    list_items.reverse()


    for i in range(number_of_words):
        most_popular_words.append(list_items[i][0])

    return(most_popular_words)

most_common_words('lorem_ipsum.txt')
print(most_common_words('lorem_ipsum.txt'))

