import numpy as np

size = (np.random.randint(2, 10), np.random.randint(2, 10))
numbers = np.random.randint(1, 25, size)

print(f'Представлен случайный двумерный массив: \n {numbers}')
print(f'Минимальное значение массива {np.min(numbers)} -> его индекс {np.argmin(numbers)}')
print(f'Максимальное значение массива {np.max(numbers)} -> его индекс {np.argmax(numbers)}')
print(f'Элементы главной диагонали матрицы в виде одномерного массива: \n {np.diagonal(numbers)}')
