
acc_email = 'art-sonil@mail.ru'
acc_log = 'AliaksandrHus'
acc_phone = '+375(29)5003900'


# БЕЗ ДЕКОРАТОРА -----------------------------------------------------------------------


def email(x): print(x)

def login(x): print(x)

def phone(x): print(x)

while True:

    print('+----+ БЕЗ ДЕКОРА +----+\n'
          '|  1 - показать почту  |\n'
          '|  2 - показать логин  |\n'
          '|  3 - показать номер  |\n'
          '|  0 - завершить цикл  |\n'
          '+----------------------+')

    choice = input('Ваш выбор: ')

    if choice == '1': email(acc_email)
    elif choice == '2': login(acc_log)
    elif choice == '3': phone(acc_phone)
    elif choice == '0': break
    else: print('Неверный ввод')


# С ИСПОЛЬЗОВАНИЕМ ДЕКОРАТОРА ---------------------------------------------------------


def decor(fun):                                         # Декоратор с запросом пароля

    def wrapper(x):                                     # Обертка декоратора

        pas = input('Введите пароль: ')                 # Ввод пароля
        print(str(fun).split()[1] + ': ', end='')       # Вывод названия функции
        if pas == '123': fun(x)                         # Проверка пароля / вызов функции
        else: print('Пароль не верный')                 # Отказ в доступе

    return wrapper                                      # Функция decor возвращает объект функцию обертку


@decor
def email(x): print(x)

@decor
def login(x): print(x)

@decor
def phone(x): print(x)


while True:

    print('+--+ С ДЕКОРАТОРОМ  +--+\n'
          '|  1 - показать почту  |\n'
          '|  2 - показать логин  |\n'
          '|  3 - показать номер  |\n'
          '|  0 - завершить цикл  |\n'
          '+----------------------+')

    choice = input('Ваш выбор: ')

    if choice == '1': email(acc_email)
    elif choice == '2': login(acc_log)
    elif choice == '3': phone(acc_phone)
    elif choice == '0': break
    else: print('Неверный ввод')

