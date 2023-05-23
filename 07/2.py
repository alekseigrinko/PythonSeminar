def get_do_it(count):
    def get_func(func):
        def decorator():
            x = count
            while x > 0:
                func()
                x = x - 1
        return decorator
    return get_func

@get_do_it(int(input('Сколько раз необходимо выполнить функцию?:')))
def function():
    print('Функция')

function()