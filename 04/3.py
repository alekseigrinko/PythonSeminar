import math

point = int(input('Введите количество знаков Пи после запятой: '))
pi = math.pi

print(f'{point} -> ' + str(round(pi, point)))
