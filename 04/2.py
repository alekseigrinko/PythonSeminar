range = ['Сливочное', 'Бурёнка', 'Вафелька', 'Сладкоежка']
on_stock = ['Сливочное', 'Вафелька', 'Сладкоежка']

def getDifference(list1, list2):
    return set(list1).difference(set(list2))

print('Закончилось: ' + ' '.join(getDifference(range, on_stock)))