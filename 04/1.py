number = int(input('Введите натуральное число N: '))

def calc(number: int):
    list = []
    n = number
    count = 0
    multiplier = 2
    while n//multiplier != 0:
        while n%multiplier == 0:
            n /= multiplier
            list.append(str(multiplier))
            count += 1
        multiplier += 1
    print(f'{number} - > ' + ' '.join(list))
    print(f'Простых множителей у числа {number}: {count}.')

calc(number)