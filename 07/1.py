def function(func, list):
    return [func(x) for x in list]

list1 = [2, 3, 5]

print(list(map(lambda x: x*2, list1)))
print(function(lambda x: x*2, list1))