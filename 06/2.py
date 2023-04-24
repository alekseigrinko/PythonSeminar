import random

def function():
    numbers = [random.randint(1, 10) for _ in range (15)]
    print(f'Задан массив из случайных цифр на 15 элементо: ' + str(numbers))
    check = True
    while check:
        n = input('Введите трёхзначное натуральное число. Для проверки, есть в массиве последовательность из трёх элементов\
              , совпадающих с введённым числом: ')
        if (len(n) == 3):
            check = False
        else: 
            print('Вы ввели не трёхзначное число, введите значение ещё раз!')
    if n in ''.join(map(str, numbers)):
        print(f'{str(numbers)} - {n} -> да')
    else: 
        print(f'{str(numbers)} - {n} -> нет')

function()