import random

def function():
    numbers = [random.randint(1, 10) for _ in range (11)]
    result = list(filter(lambda x: x > 5, numbers))
    print(', '.join(map(str, numbers)) + ' -> ' + ', '.join(map(str, result)))

function()