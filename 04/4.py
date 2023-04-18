polynomial1 = '5x^2 + 3x'
polynomial2 = '8x^2 + 4x + 8'

def parc(list, list_x2, list_x, list_n):
    x = 0
    while x < len(list):
        if 'x^2' in list[x]:
            if x > 0:
                list_x2.append(list[x-1])
                list_x2.append(list[x])
                list.pop(x)
                list.pop(x-1)
            else: 
                list_x2.append('+')
                list_x2.append(list[x])
                list.pop(x)
        elif 'x' in list[x]:
            if x > 0:
                list_x.append(list[x-1])
                list_x.append(list[x])
                list.pop(x)
                list.pop(x-1)
            else:
                list_x.append('+') 
                list_x.append(list[x])
                list.pop(x)
        elif ('+' in list[x]) or ('-' in list[x]):
            x += 1
        else:
            if x > 0:
                list_n.append(list[x-1])
                list_n.append(list[x])
                list.pop(x)
                list.pop(x-1)
            else:
                list_n.append('+')
                list_n.append(list[x])
                list.pop(x)
    return list_x2, list_x, list_n

def sum(list):
    count = 0
    x = 0
    substr = list[1][1:]
    while x < len(list):
        if ('+' in list[x]):
            count += int(list[x+1][0])
            list.pop(x)
            list.pop(x)
        else:
            count -= int(list[x+1][0])
            list.pop(x)
            list.pop(x)
    if count > 0:
        return '+ ' + str(count) + substr + ' '
    else:
        return ' ' + str(count) + substr + ' '
    
def format(line1, line2, line3):
    if '+' in line1[0]:
        return line1[2:] + line2 + line3
    else:
        return line1 + line2 + line3


def calc(polynomial1: str, polynomial2: str):
    list_x2 = []
    list_x = []
    list_n = []
    list_x2, list_x, list_n = parc(polynomial1.split(), list_x2, list_x, list_n)
    list_x2, list_x, list_n = parc(polynomial2.split(), list_x2, list_x, list_n)
    print(format(sum(list_x2) ,sum(list_x) ,sum(list_n)))

calc(polynomial1, polynomial2)
