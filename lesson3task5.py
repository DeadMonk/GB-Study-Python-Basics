# -*- coding: utf-8 -*-
# !/usr/bin/python3


from random import choices, sample


def get_jokes(count=1, uniq=False):
    """
    Выдаёт набор шуток в количестве равном count.

    :param count: Количество шуток
    :param uniq: Флаг не дающий использовать слово в разных шутках. Если включён, количество не более 5.
    :return:
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if uniq:
        nouns = sample(nouns, 5)
        adverbs = sample(adverbs, 5)
        adjectives = sample(adjectives, 5)
        for joke in zip(nouns, adverbs, adjectives):
            joke_list.append(' '.join(sample(joke, 3)))
    else:
        nouns = choices(nouns, k=count)
        adverbs = choices(adverbs, k=count)
        adjectives = choices(adjectives, k=count)
        for joke in zip(nouns, adverbs, adjectives):
            joke_list.append(' '.join(sample(joke, 3)))
    return sample(joke_list, count)
