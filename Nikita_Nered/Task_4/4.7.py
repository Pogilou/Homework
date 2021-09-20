def foo (list_for_multiplication):
    list_after_multiplication = []
    for i in range(len(list_for_multiplication)):
        result = 1
        for num, k in enumerate(list_for_multiplication):
            if num == i:
                continue
            result *= k
        list_after_multiplication.append(result)
    return (list_after_multiplication)

print(foo([1, 2, 3, 4, 5]))