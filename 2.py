
# 1 Пример декоратора с передачей аргументов ++++++++++++++++++++++++++++++++++

def dec(func):
    def wrapper(x, y):
        print('+-- инструкции обетрки --+')
        func(x, y)
        print('+-- инструкции обетрки --+\n' + '-' * 26)
    return wrapper


@dec
def test(a, b):
    print(a, b, f'{1:>4}')


test('1 аргумент', '2 аргумент')


# 2 Пример декоратора с передачей запакованных аргументов +++++++++++++++++++++

def dec(func):
    def wrapper(*args):
        print('+-- инструкции обетрки --+')
        func(*args)
        print('+-- инструкции обетрки --+\n' + '-' * 26)
    return wrapper


@dec
def test(a, b, c):
    print(a, b, c, f'{2:>7}')


test('1 один', '2 два', '3 три')


# 3 Пример декоратора с передачей ключевых аргументов +++++++++++++++++++++++++

def dec(func):
    def wrapper(**kwargs):
        print('+-- инструкции обетрки --+')
        func(**kwargs)
        print('+-- инструкции обетрки --+\n' + '-' * 26)
    return wrapper


@dec
def test(a, b):
    print(a, b, f'{3:>4}')


test(b='1 аргумент', a='2 аргумент')


# 4 Пример декоратора с передачей запакованных и ключевых аргументов ++++++++++

def dec(func):
    def wrapper(*args, **kwargs):
        print('+-- инструкции обетрки --+')
        func(*args, **kwargs)
        print('+-- инструкции обетрки --+\n' + '-' * 26)
    return wrapper


@dec
def test(a, b):
    print(a, b, f'{4:>4}')

test('1 аргумент', b='2 аргумент')


# 5 Пример декоратора с передачей аргументов и возвратом значения +++++++++++++

def dec(func):
    def wrapper(*args, **kwargs):
        print('+-- инструкции обетрки --+')
        res = func(*args, **kwargs)
        print('+-- инструкции обетрки --+')
        return res
    return wrapper


@dec
def test(a, b, c, d):
    print(f'{a} + {b} + {c} + {d} =', a + b + c + d, f'{5:>2}')
    return sum([a, b, c, d])


res = test(10, 20, c=30, d=40)
print('\nРезультат =', res)
