import random

def head():
    print("---------------------")
    print("| Крестики - нолики |")
    print("---------------------")

def check(line1, line2, line3):
    options = ['x', 'o']
    key = True
    count = 0
    for i in options:
        if (i in line1[0] and i in line1[1] and i in line1[2]) or\
        (i in line2[0] and i in line2[1] and i in line2[2]) or\
        (i in line3[0] and i in line3[1] and i in line3[2]) or\
        (i in line1[0] and i in line2[0] and i in line3[0]) or\
        (i in line1[1] and i in line2[1] and i in line3[1]) or\
        (i in line1[2] and i in line2[2] and i in line3[2]) or\
        (i in line1[0] and i in line2[1] and i in line3[2]) or\
        (i in line1[2] and i in line2[1] and i in line3[0]):
            print(f'{i} - победили!')
            playing_field(line1, line2, line3)
            key = False
        for x in range(3):
            if i in line1[x]:
                count += 1
            if i in line2[x]:
                count += 1
            if i in line3[x]:
                count += 1
    if (count == 9):
        print('Ничья!')
        playing_field(line1, line2, line3)
        key = False
    return key

def check_field(line1, line2, line3, n: int, player):
    key = True
    if n > 9 or n < 1:
        print('Введено некорректное значение!')
    elif n == 1:
        if '1' in line1[0]:
            line1[0] = player
            key = False
        else:
            print('По указанному полю был уже ход игрока!')
    elif n == 2:
        if '2' in line1[1]:
            line1[1] = player
            key = False
        else:
            print('По указанному полю был уже ход игрока!')
    elif n == 3:
        if '3' in line1[2]:
            line1[2] = player
            key = False
        else:
            print('По указанному полю был уже ход игрока!')
    elif n == 4:
        if '4' in line2[0]:
            line2[0] = player
            key = False
        else:
            print('По указанному полю был уже ход игрока!')
    elif n == 5:
        if '5' in line2[1]:
            line2[1] = player
            key = False
        else:
            print('По указанному полю был уже ход игрока!')
    elif n == 6:
        if '6' in line2[2]:
            line2[2] = player
            key = False
        else:
            print('По указанному полю был уже ход игрока!')
    elif n == 7:
        if '7' in line3[0]:
            line3[0] = player
            key = False
        else:
            print('По указанному полю был уже ход игрока!')
    elif n == 8:
        if '8' in line3[1]:
            line3[1] = player
            key = False
        else:
            print('По указанному полю был уже ход игрока!')
    elif n == 9:
        if '9' in line3[2]:
            line3[2] = player
            key = False
        else:
            print('По указанному полю был уже ход игрока!')
    return line1, line2, line3, key

def check_field_bot(line1, line2, line3, n: int, player):
    key = True
    if n == 1:
        if '1' in line1[0]:
            line1[0] = player
            key = False
    elif n == 2:
        if '2' in line1[1]:
            line1[1] = player
            key = False
    elif n == 3:
        if '3' in line1[2]:
            line1[2] = player
            key = False
    elif n == 4:
        if '4' in line2[0]:
            line2[0] = player
            key = False
    elif n == 5:
        if '5' in line2[1]:
            line2[1] = player
            key = False
    elif n == 6:
        if '6' in line2[2]:
            line2[2] = player
            key = False
    elif n == 7:
        if '7' in line3[0]:
            line3[0] = player
            key = False
    elif n == 8:
        if '8' in line3[1]:
            line3[1] = player
            key = False
    elif n == 9:
        if '9' in line3[2]:
            line3[2] = player
            key = False
    return line1, line2, line3, key

def print_line(line):
    print('|' + '|'.join(line) + '|')

def playing_field(line1, line2, line3):
    print_line(line1)
    print_line(line2)
    print_line(line3)

def menu(line1, line2, line3):
    print('Добро пожаловать в крестики-нолики!')
    player = ''
    bot = ''
    key = True
    while key:
        n = input('Введите 1 для игры X-ками \nВведите 2 для игры O-ками\n ----->  ')
        if int(n) == 1:
            player = 'x'
            bot = 'o'
            key = False
        elif int(n) == 2:
            player = 'o'
            bot = 'x'
            key = False
        else:
            print('Введено некорректное значение!')
    key = True
    v = random.randint(1,3)
    if v == 1:
        print('Игрок ходит первым!')
        playing_field(line1, line2, line3)
        while key:
            line1, line2, line3 = playing_player(line1, line2, line3, player)
            key = check(line1, line2, line3)
            if key:
                line1, line2, line3 = playing_bot(line1, line2, line3, bot)
                key = check(line1, line2, line3)
    else:
        print('Игрок ходит вторым!')
        while key:
            line1, line2, line3 = playing_bot(line1, line2, line3, bot)
            key = check(line1, line2, line3)
            if key:
                line1, line2, line3 = playing_player(line1, line2, line3, player) 
                key = check(line1, line2, line3)

def playing_player(line1, line2, line3, player):
    key = True
    while key:
        n = int(input('Введите номер поля для дальшейго хода: '))
        line1, line2, line3, key = check_field(line1, line2, line3, n, player)
    return line1, line2, line3

def playing_bot(line1, line2, line3, bot):
    key = True
    while key:
        n = random.randint(1,9)
        line1, line2, line3, key = check_field_bot(line1, line2, line3, n, bot)
    playing_field(line1, line2, line3)
    return line1, line2, line3

def function():
    line1 = ['1', '2', '3']
    line2 = ['4', '5', '6']
    line3 = ['7', '8', '9']
    head()
    menu(line1, line2, line3)
    
function()