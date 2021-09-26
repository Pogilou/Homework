file = open('unsorted_names.txt', 'r')

names = []

for line in file:
    names.append(line)

file.close()

names.sort()

f = open('sorted_names.txt', 'w')

for name in names:
    f.write(name)

f.close()
