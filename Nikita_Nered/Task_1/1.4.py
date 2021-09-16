print ("Enter the number: ")
number = int(input())
dividers = []

for i in range(1, number):
    if number % i == 0:
        dividers.append(i)
print(set(dividers))

