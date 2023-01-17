
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
