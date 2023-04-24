def function():
    min = 0
    max = 1
    result = []
    print('Все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11: ')
    for i in range (1, 11):
        for y in range (1, 12):
            if (i//y < 1):
                if (i%2!=0 or y%2!=0) and (i%3!=0 or y%3!=0) and (i%5!=0 or y%5!=0):
                    if (str(i)+'/'+str(y)) not in result:
                        result.append(str(i)+'/'+str(y))
    print(', '.join(result))

function()