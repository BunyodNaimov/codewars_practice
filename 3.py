"""
Вы в зоопарке... все сурикаты выглядят странно.
Что-то пошло ужасно не так – кто-то поменялся местами!

Спасите животных, переключив их обратно. Вам будет предоставлен массив,
который будет иметь три значения (хвост, тело, голова).
Ваша задача — перестроить массив так, чтобы животное располагалось правильно
(голова, тело, хвост).

То же самое касается всех остальных массивов/списков, которые вы получите в тестах:
вам нужно изменить позиции элементов с той же самой логикой.

Просто!
test.assert_equals(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
"""


def fix_the_animals(array):
    # Обмен значениями первого и третьего элементов
    array[0], array[2] = array[2], array[0]
    return array
