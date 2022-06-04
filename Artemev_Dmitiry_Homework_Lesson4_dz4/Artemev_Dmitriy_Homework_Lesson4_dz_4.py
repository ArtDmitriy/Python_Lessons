# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

import sys

import utils


if __name__ == "__main__":

    args = sys.argv[1:]

    for code in args:
        conv = utils.currency_rates(code)
        if conv:
            cur, date = conv
            date = date.strftime("%d-%m-%Y")
            print(f"{cur}, {date}")