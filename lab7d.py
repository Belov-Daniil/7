# У няни 7 разных фруктов (ф1,…ф7).
# Сформировать (вывести) все возможные варианты меню полдника
# (1 фрукт) для ребенка на неделю.
# Доп. условие
# киви должно стоять в неделе раньше яблока а ананас позже
from itertools import *
import numpy as np


class Schedule:
    def __init__(self):
        self.fruit_basket = ['apple', 'pineapple', 'orange', 'banana', 'pear', 'kiwi', 'avocado']

    def count_rec(self):
        n = self.rec()
        p = 0
        for i in n:
            if len(i) == 7 and len(np.unique(i)) == 7:
                if i.index('kiwi') < i.index('apple') > i.index('pineapple'):
                    pass
                else:
                    p += 1
                    print(*i)
        print('общее кол-во вариантов меню на неделю : ' + str(p))

    def count_iter(self):
        n = self.iter()
        p = 0
        for i in n:
            if len(i) == 7 and len(np.unique(i)) == 7:
                if i.index('kiwi') < i.index('apple') > i.index('pineapple'):
                    pass
                else:
                    p += 1
                    print(*i)
        print('общее кол-во вариантов меню на неделю : ' + str(p))

    def iter(self):
        all_variants = []
        for i in permutations(self.fruit_basket, 7):
            all_variants.append(i)
        return all_variants

    def rec(self, k=7):
        if k == 1:
            return [[x] for x in self.fruit_basket]
        else:
            return [[x] + y for x in self.fruit_basket for y in self.rec(k - 1)]


def start():
    print(
        'У няни 7 разных фруктов (ф1,…ф7). Сформировать (вывести) все возможные варианты меню полдника (1 фрукт)'
        ' для ребенка на неделю.')
    print(
        'Спустя некоторое время няня поняла что если поставить в распивании киви после яблока а ананас до то у ребёнка'
        ' несварение. Поэтому  ')
    print('киви должно стоять в неделе раньше яблока а ананас после')
    s = Schedule()
    a = input('Напишите rec для рекурсивного решения, iter для итеративного \n')
    while a != 'rec' and a != 'iter':
        a = input('Напишите rec для рекурсивного решения, iter для итеративного \n')
    if a == 'rec':
        s.count_rec()
        b = ''
        while b != 'rerun' and b != 'exit':
            b = input('чтобы начать заного напишите rerun, чтобы закрыть программу напишите exit \n')
        if b == 'rerun':
            start()
        else:
            exit()
    else:
        s.count_iter()
        b = ''
        while b != 'rerun' and b != 'exit':
            b = input('чтобы начать заного напишите rerun, чтобы закрыть программу напишите exit \n')
        if b == 'rerun':
            start()
        else:
            exit()


start()
