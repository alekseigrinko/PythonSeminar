fruits = []
key = True
while key:
    n = int(input("Введите 1 для добавления фрукта в список либо 0 для выхода: "))
    if n == 0:
        key = False
    else:
        fruits.append(input("Введите название фрукта: "))

litter = str(input('Введите первую букву названия фрукта для отбора: '))

def filter(litter: str, fruits: list):
    result = []
    for index in range(len(fruits)):
        if fruits[index][0] == litter:
            result.append(fruits[index])
    return result

print(f'{litter} -> ' + ' '.join(filter(litter, fruits))) 



