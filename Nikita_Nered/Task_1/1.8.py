a = 3
b = 11

c = 3
d = 10

new = ['']
for i in range (c,d+1):
    new.append(i)

for i in new:
    print("%4s" % i, end='')

print ("")

for i in range(a,b+1):
    print("%4d" % i, end='')
    for k in range (c,d+1):
        x = i * k
        print("%4d" % x, end='')
    print()