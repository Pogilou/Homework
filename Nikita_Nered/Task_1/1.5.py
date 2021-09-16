slovar = {'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
keys = list(slovar.keys())
keys.sort()
new_slovar = {}

for i in keys:
    new_slovar[i] = slovar[i]

print(new_slovar)