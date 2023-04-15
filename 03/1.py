number = int(input("Введите необходимое количество первых элементов последовательности Фибоначчи: "))

def fibonacci(number):
    numbers = []
    for i in range(1, number+1):
        if i < 3:
            numbers.append(1)
        else:
            numbers.append(numbers[i-2]+numbers[i-3])
    return numbers

print(f'{number} -> ' + ' '.join(map(str, fibonacci(number))))