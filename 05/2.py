import random
def getResult(numbers):
    n = i = 0
    numbers = sorted(numbers)
    result = []
    while n < len(numbers):
        if n == 0:
            n = random.randint(n, n + 3)
            result.append(numbers[n])
            i += 1
            n += random.randint(n + 1, n + 3)
        elif numbers[n] > result[i-1]:
            result.append(numbers[n])
            i += 1
            n += random.randint(n + 1, n + 3)
        elif numbers[n] == result[i-1]:
            n += random.randint(n + 1, n + 3)
    return result

def getResult2(numbers): #без сортировки
    n = i = 0
    result = []
    check = True
    while n < len(numbers):
        if n == 0:
            while check:
                n = random.randint(n, len(numbers) - 1)
                if numbers[n] < max(numbers):
                    result.append(numbers[n])
                    n = random.randint(1,  3)
                    check = False
            i += 1
        elif numbers[n] > result[i-1]:
            result.append(numbers[n])
            i += 1
            n += random.randint(n + 1, n + 3)
        elif numbers[n] <= result[i-1]:
            n += random.randint(n + 1, n + 3)
    if (len(result) == 1):
        result.append(max(numbers))
    return result   

def function():
    numbers = [random.randint(1, 10) for _ in range (11)]
    print(str(numbers) + ' => ' + str(getResult(numbers)))
    print(str(numbers) + ' => ' + str(getResult2(numbers)))

function()