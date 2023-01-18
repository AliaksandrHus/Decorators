
# Передача дополнительных параметров в декоратор ++++++++++++++++++++++++++++++

def decor(x):
    def outer(func):
        def wrapper():
            print(f'{x}! ---- !{x}')
            func()
            print(f'{x}! ---- !{x}\n')
        return wrapper
    return outer


@decor('NEW')
def test():
    print('пример функции')

test()

# Вызов с дополнительными параметрами в декоратор +++++++++++++++++++++++++++++


def test():
    print('пример функции')

x = decor(' 1 ')(test)
x()

test = decor(' 2 ')(test)
test()


# Декорирование нескольких функций одновременно +++++++++++++++++++++++++++++++

def groop(*func):
    def wrapper():
        print('+++ инструкции обертки +++')
        for function in func: function()
        print('+++ инструкции обертки +++\n')
    return wrapper


def one(): print('...   Первая функция   ...')

def two(): print('...   Вторая функция   ...')

def three(): print('...   Третья функция   ...')


all_func = groop(one, two, three)
all_func()


two_func = groop(one, two)
two_func()

one_func = groop(one)
one_func()


# Изменение параметров функций с помощью декоратора++++++++++++++++++++++++++++

def dec(func):
    def wrapper(*args):

        print('Вход:', args)
        if args: new = [x if x > 0 else 1 for x in args]; print('Выход: ', end=''); func(*new)
        else: func(*args)

    return wrapper


@dec
def temp(x, y):
    print(x, y, '\n')


temp(100, 200)

temp(-5, - 10)

temp(-20, 30)


