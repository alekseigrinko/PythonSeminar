def function():
    number = int(input("Введите число: "))
    numbers = list()
    count = int(1)
    for i in range(1, number+1):
        count *= int(i)
        numbers.append(str(count))
    print(f"{number} -> [" + ', '.join(numbers) + "]")
function()