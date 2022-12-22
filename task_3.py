# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint, random

list = [1, 2, 3, 4, 5, 6, 7]

print(f'Исходный список --> *{list}*', sep=', ')


def mix_list(list):
    len_list = len(list)
    for i in range(len_list):
        sum = randint(0, len_list - 1)
        temp = list[i]
        list[i] = list[sum]
        list[sum] = temp
    return list


mixed_list = mix_list(list)

print(f'Перемешанный список --> *{list}*', sep=', ')
