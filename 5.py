
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