def get_shortest_word(s: str):
    s = s.split()
    long_words = 0
    for i in s:
        if len(i) > long_words:
            long_words = len(i)
            word = i

    return (word)

print(get_shortest_word("Any pythonista like namespaces a lot."))
