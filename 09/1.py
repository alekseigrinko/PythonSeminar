import numpy as np

size = (25)
numbers = list(np.random.randint(1, 30, size))
uniq_elements = list(np.unique(numbers))
count = uniq_elements.__len__()
print(f'Представлен список элементов: \n {numbers} \n В нем {count} уникальных элементов: \n {uniq_elements}')