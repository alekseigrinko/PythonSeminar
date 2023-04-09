number = int(input("Введите число: "))
numbers = list()
for i in range(1, number + 1):
    if i%2 == 0:
        numbers.append(str(i))
print(f'{number} -> ' + ', '.join(numbers))