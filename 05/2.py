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
        if numbers[n] > result[i-1]:
            result.append(numbers[n])
            i += 1
            n += random.randint(n + 1, n + 3)
    return result   

def function():
    numbers = [random.randint(1, 10) for _ in range (11)]
    print(str(numbers) + ' => ' + str(getResult(numbers)))

function()