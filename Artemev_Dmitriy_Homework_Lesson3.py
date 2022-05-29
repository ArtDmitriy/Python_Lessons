# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

DICT_NUM = {

    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четире",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
}


def num_translate(num_word):
    """ convert one to один...nine to девять """
    return DICT_NUM.get(num_word)


def num_translate_adv(num_word):
    """ convert one to один...nine to девять with firt char capitalize """
    to_key = DICT_NUM.get(num_word.lower())

    if to_key:
        return to_key.capitalize() if num_word[0].isupper() else to_key

    return None


# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }


def thesaurus(*args):
    """ convert name list to dictionary like {A: [Ivan..] , B:[Maria..]} """
    out_dict = {}

    for name in args:

        if out_dict.get(name[0]):
            out_dict[name[0]].append(name)
        else:
            out_dict[name[0]] = [name]

    return out_dict


# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.


from random import choice


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def gen(from_, used_, unique):
    while True:
        n_nouns = choice(from_)

        if not (unique and n_nouns in used_):
            used_.append(n_nouns)
            break

    return (n_nouns, used_)

def get_jokes(count, unique=False):
    """ gen count jokes """
    used = []
    answer = []

    # if we used unique flag need protect

    if unique and count < len([*nouns, *adverbs, *adjectives]):
        return []
    for _ in range(count):
        nons, used_ = gen(nouns, used, unique)
        used.append(used_)

        adv, used_ = gen(adverbs, used, unique)
        used.append(used_)

        adj, used_ = gen(adjectives, used, unique)
        used.append(used_)

        answer.append(f"{nons} {adv} {adj}")

    return answer
