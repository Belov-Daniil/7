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
        self.fruit_names = []

    def count_rec(self):
        n = self.rec()
        p = 0
        for i in n:
            if len(i) == 7 and len(np.unique(i)) == 7:
                if not (i.index(self.fruit_names[0]) < i.index(self.fruit_names[1]) < i.index(self.fruit_names[2])):
                    continue
                else:
                    p += 1
                    print(*i)
        print('общее кол-во вариантов меню на неделю : ' + str(p))

    def count_iter(self):
        n = self.iter()
        p = 0
        for i in n:
            if len(i) == 7 and len(np.unique(i)) == 7:
                if not (i.index(self.fruit_names[0]) < i.index(self.fruit_names[1]) < i.index(self.fruit_names[2])):
                    continue
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
    s = Schedule()
    a = input('Напишите rec для рекурсивного решения, iter для итеративного \n')
    while a != 'rec' and a != 'iter':
        a = input('Напишите rec для рекурсивного решения, iter для итеративного \n')
    if a == 'rec':
        print(
            'В качестве усложнения составления расписания напишите три фрукта из представленных на выбор:'
            ' apple, pineapple, orange, banana, pear, kiwi, avocado'
            ' Они будут стоять в меню таким обазом - Фрукт 1 будет всегда до фрукта 2, а фрукт 3 будет после фрукта 2')
        fruits_name = input().split(' ')
        while len(fruits_name) < 3 or fruits_name[1] not in s.fruit_basket or fruits_name[0] \
                not in s.fruit_basket or fruits_name[2] not in s.fruit_basket:
            fruits_name = input(' напишите три фрукта из представленных на выбор: apple, pineapple,'
                                ' orange, banana, pear, kiwi, avocado\n').split(' ')
        s.fruit_names = fruits_name
        s.count_rec()
        b = ''
        while b != 'rerun' and b != 'exit':
            b = input('чтобы начать заного напишите rerun, чтобы закрыть программу напишите exit \n')
        if b == 'rerun':
            start()
        else:
            exit()
    else:
        print(
            'В качестве усложнения составления расписания напишите три фрукта из представленных на выбор:'
            ' apple, pineapple, orange, banana, pear, kiwi, avocado'
            ' Они будут стоять в меню таким обазом - Фрукт 1 будет всегда до фрукта 2, а фрукт 3 будет после фрукта 2')
        fruits_name = input().split(' ')
        while len(fruits_name) < 3 or fruits_name[1] not in s.fruit_basket or fruits_name[0] \
                not in s.fruit_basket or fruits_name[2] not in s.fruit_basket:
            fruits_name = input(' напишите три фрукта из представленных на выбор: apple, pineapple,'
                                ' orange, banana, pear, kiwi, avocado\n').split(' ')
        s.fruit_names = fruits_name
        s.count_iter()
        b = ''
        while b != 'rerun' and b != 'exit':
            b = input('чтобы начать заного напишите rerun, чтобы закрыть программу напишите exit \n')
        if b == 'rerun':
            start()
        else:
            exit()


start()
