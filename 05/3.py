import random
def getResult(numbers):
    n = 0
    result = list(numbers)
    duplicates = []
    count = 0
    while n < len(result):
        x = result[n]
        y = n + 1
        while y < len(result):
            if x == result[y]:
                if x not in duplicates:
                    duplicates.append(x)
                result.pop(y)
                count += 1
            else:
                y += 1
        n += 1            
    print(str(numbers) + ' => ' + f'{count} элемента совпадают')
    print('Список уникальных элементов => ' + str(result))


def function():
    numbers = [random.randint(1, 10) for _ in range (15)]
    getResult(numbers)
function()