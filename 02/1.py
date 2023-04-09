number = int(input("Введите число: "))
numbers = list()
count = None
for i in range(1, number+1):
    if i == 1:
        count = int(i)
    else:
        count *= int(i)
    numbers.append(str(count))
print(f"{number} -> [" + ', '.join(numbers) + "]")