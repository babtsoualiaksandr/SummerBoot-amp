import random
import re

def get_random_word() -> str:
    words = ('епам', 'лето', 'змея', 'лекция', 'учеба', 'задания', 'язык', 'английский',
         'вебинар', 'книги', 'документация', 'получение', 'удаленная', 'работа', 'успех', 'спасибо')
    random.seed()
    return words[random.randint(0, len(words)-1)]
