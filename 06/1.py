def function():
    n = input('Введите натуральное число N: ')
    n2 = n + n
    n3 = n2 + n
    print(f'Значение выражения:N + NN + NNN, равно:\n\
          N = {n}: {n} + {n2} + {n3} = {int(n) + int(n2) + int(n3)}')

function()