from dataclasses import dataclass
import random
import re

from enum import Enum

StateGame = Enum('StateGame', 'continues losing success')


class GameGallow:
    """
     [summary]

    [extended_summary]
    """

    def __init__(self) -> None:
        words = ('епам', 'лето', 'змея', 'лекция', 'учеба', 'задания', 'язык', 'английский',
                 'вебинар', 'книги', 'документация', 'получение', 'удаленная', 'работа', 'успех', 'спасибо')
        random.seed()
        self.word_sought = words[random.randint(0, len(words)-1)]
        self.word_unknown = '-'*len(self.word_sought)
        self.errors = 0
        self.errors_max = 10
        self.state = StateGame.continues

    def trying_guess(self, letter: str) -> str:
        """
        trying_guess [summary]

        [extended_summary]

        :param letter: [description]
        :type letter: str
        :return: [description]
        :rtype: str
        """
        if not self.state == StateGame.continues:
            return f'Game over {self.state} click /start or /exit'
        if (not len(letter) == 1) | letter.isdigit():
            return f'Error input... <{letter}> pls enter ONE letter '
        indexes_find = [m.start()
                        for m in re.finditer(letter, self.word_sought)]
        if len(indexes_find) == 0:
            self.errors += 1
            msg = f'There is no such letter {letter} in the word {self.word_unknown} Attempts left {self.errors_max-self.errors}\n'
            if self.errors >= self.errors_max:
                self.state = StateGame.losing
                msg += '\U0001F614'
                msg += f"You didn't guess the word <{self.word_sought}> <{self.word_unknown}> {msg}"
            return msg
        else:
            list_word_unknown = list(self.word_unknown)
            for idx in indexes_find:
                list_word_unknown[idx] = letter
            self.word_unknown = "".join(list_word_unknown)
            msg = f'There is such a letter!!!  {self.word_unknown} \n'
            if self.word_sought == self.word_unknown:
                self.state = StateGame.success
                msg += f'Congratulations, you guessed the word <{self.word_unknown}>'
            return msg

    def __str__(self):
        return f'word_unknown: {self.word_unknown} \nword_sough: {self.word_sought}\nerrors {self.errors} \nstatus: {self.state.name}\n\n'

    def check(self):
        return self.state


def letter_from_player(id_player: str, letter: str, players_games) -> str:
    if id_player in players_games:
        player_game = players_games[id_player]
        return player_game.trying_guess(letter.lower())
    else:
        return 'Pls click /start'


__author__ = "Aliaksandr Babtsou"
__copyright__ = "Copyright 2021, The Summer Bootcamp"