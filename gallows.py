#!python3

"""
     "Виселица"
"""

import random
import re

words = ('епам', 'лето', 'змея', 'лекция', 'учеба', 'задания', 'язык', 'английский',
         'вебинар', 'книги', 'документация', 'получение', 'удаленная', 'работа', 'успех', 'спасибо')

random.seed()
index = random.randint(0, len(words)-1)
word_sought = words[index]
len_word = len(word_sought)
word_unknown = '-' * len_word
error = 0
while error < 11:
    if word_unknown == word_sought:
        break
    input_letter = input(
        f'Enter a letter in word <{word_unknown}> pls : ').lower()
    if not len(input_letter) == 1:
        print('Input ONE letter')
        continue
    indexes_find = [m.start() for m in re.finditer(input_letter, word_sought)]
    if len(indexes_find) == 0:
        error += 1
        print('Error')
        continue
    list_word_unknown = list(word_unknown)
    for idx in indexes_find:
        list_word_unknown[idx] = input_letter
        word_unknown = "".join(list_word_unknown)
result = f'Game Over!! The word {word_sought} is not guessed' if error == 11 else f'Congratulations!!! The word is guessed {word_unknown}'
print(result)

__author__ = "Aliaksandr Babtsou"
__copyright__ = "Copyright 2021, The Summer Bootcamp"
