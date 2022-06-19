# Урок 8. Декораторы.


# 1. Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и
# возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.
# Пример:

# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

import re


VALID_RE = re.compile(
    r"(?P<username>[a-zA-Z0-9\.\-\_]+)@(?P<domain>[a-zA-Z0-9\.\-\_]+)")


def email_parse(email):
    """ validation of email """
    try:
        test = map(lambda x: x.groupdict(), VALID_RE.finditer(email))
        print(test.__next__())
    except:
        raise ValueError from ValueError

# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>


# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:

# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


from functools import wraps


def type_logger(level=0):

    def logger(func):

        @wraps(func)
        def decor(*argv, **kwargs):

            all_args = list(argv) + list(kwargs.values())
            norm_res = func(all_args[0])

            if level == 1:
                print(", ".join([f"{x}:{type(x)}" for x in all_args]))
            elif level == 2:
                print(f"{func.__name__}:{type(func)}")
                print(f"{func.__name__}({all_args[0]}):{type(norm_res)}")

            return norm_res

        return decor

    return logger


@type_logger(2)
def calc_cube(x):
    """ cube of args """
    return x ** 3


if __name__ == "__main__":
    a = calc_cube(5, 6, 7, 8, 9, 1, 2, 3, val1=4, val2=5)
    print(a)


# 4. Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так,
# например:

# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5



from functools import wraps

def val_checker(func_filter):

    def checker(func):

        @wraps(func)
        def decor(x):

            if func_filter(x):
                return func(x)

            raise ValueError from ValueError

        return decor

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3