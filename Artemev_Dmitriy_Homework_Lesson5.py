# Урок 5. Генераторы и comprehensions. Множества.

# Задание №1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

def odd_num(to):
    for i in range(1, to + 1, 2):
        yield i


if __name__ == "__main__":
    a_gen = odd_num(15)

    print("a_gen type", type(a_gen))

    for elem in a_gen:
        print(elem)

    print(f"empty {list(a_gen)}")


# Задание №3. Есть два списка:

# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]

# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...

# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде:
# (<tutor>, None),
# например:
# ('Станислав', None)
#
# ### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.


def gen_new_list(tutors, klasses):
    i = 0
    while i < len(tutors) and i < len(klasses):
        yield tutors[i], klasses[i]
        i += 1
    while i < len(tutors):
        yield tutors[i], None
        i += 1

tutors = [

    'Иван', 'Анастасия', 'Петр', 'Сергей',

    'Дмитрий', 'Борис', 'Елена'

]
klasses = [

    '9А', '7В', '9Б', '9В', '8Б', '10А',
    # '10Б', '9А'
]

for i in gen_new_list(tutors, klasses):
    print(i)

if __name__ == '__main__':
    gen = gen_new_list(tutors, klasses)
    print("gen_new_list", type(gen))


# Задание №4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```
#
# Подсказка: использовать возможности python, изученные на уроке.


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []


for i in range(len(src)-1):
    if src[i] < src[i+1]:
        result.append(src[i+1])

print(result)


# Задание №5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]


import time  # use for test
import sys  # use for test


def my_set(*argv):
    """ return unique elemts of argv """
    answ = set()

    for elem in argv:
        if not elem in answ:
            answ.add(elem)
        else:
            answ.remove(elem)

    return [x for x in argv if x in answ]  # best
    #return [ x for x in argv if argv.count(x) == 1 ] # worst
    #return [ x for i, x in enumerate(argv) if not x in [*argv[:i], *argv[i+1:]] ] # bad

if __name__ == "__main__":
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [23, 1, 3, 10, 4, 11]

    t = time.perf_counter()
    r = my_set(*src)

    print("mem: ", sys.getsizeof(r))
    print("time: ", time.perf_counter() - t)

    print(r == result)
    print(r)
