import numpy as np

size = (5, 5)
numbers = np.random.randint(1, 3, size)
count = np.count_nonzero(np.corrcoef(numbers) == 1.0)
print(f'Представлен двумерный массив 5 х 5: \n {numbers}')
if (np.array(numbers).__len__() < count):
    print('В массиве имеются одинаковые строки')
else:
    print('В массиве нет одинаковых строк')