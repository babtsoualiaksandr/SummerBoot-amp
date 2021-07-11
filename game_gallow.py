from dataclasses import dataclass
import random
import re


def get_random_word() -> str:
    words = ('епам', 'лето', 'змея', 'лекция', 'учеба', 'задания', 'язык', 'английский',
             'вебинар', 'книги', 'документация', 'получение', 'удаленная', 'работа', 'успех', 'спасибо')
    random.seed()
    return words[random.randint(0, len(words)-1)]


class PlayerGame:
    def __init__(self) -> None:
        words = ('епам', 'лето', 'змея', 'лекция', 'учеба', 'задания', 'язык', 'английский',
                 'вебинар', 'книги', 'документация', 'получение', 'удаленная', 'работа', 'успех', 'спасибо')
        random.seed()
        self.word_sought = words[random.randint(0, len(words)-1)]
        self.word_unknown = '-'*len(self.word_sought)
        self.errors = 0
        self.errors_max = 50
        self.state = 'continues'

    def trying_guess(self, letter: str) -> str:
        if not self.state == 'continues':
            return f'Game over {self.state}'
        if (not len(letter) == 1) | letter.isdigit():
            return f'Error input... <{letter}> pls ONE letter '

        indexes_find = [m.start()
                        for m in re.finditer(letter, self.word_sought)]
        if len(indexes_find) == 0:
            self.errors += 1
            msg = f'There is no such letter {letter} in the word {self.word_unknown} Attempts left {self.errors_max+1-self.errors}\n'
            if self.errors > self.errors_max:
                self.state = 'losing'
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
                self.state = 'success'
                msg += f'Congratulations, you guessed the word <{self.word_unknown}>'
            return msg

    def __str__(self):
        return f'word_unknown: {self.word_unknown} \nword_sough: {self.word_sought}\nerrors {self.errors} \nstatus: {self.state}'

    def check(self):
        return self.state


def letter_from_player(id_player: str, letter: str, players_games) -> str:
    player_game = players_games.setdefault(id_player, PlayerGame())
    return player_game.trying_guess(letter.lower())


def test():
    players_games = {}
    letters = list('АБ1В6ГД7ЕЖ8ЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ')

    for iter in range(100):
        random.seed()
        letter = letters[random.randint(0, len(letters)-1)]
        print(letter)

        print(letter_from_player('00001', letter.lower(), players_games))
        random.seed()
        letter = letters[random.randint(0, len(letters)-1)]
        print(letter)
        print(letter_from_player('00002', letter.lower(), players_games))
        random.seed()
        letter = letters[random.randint(0, len(letters)-1)]
        print(letter)
        print(letter_from_player('00003', letter.lower(), players_games))

        print(letter_from_player('00001', letter.lower(), players_games))

    for key in players_games:
        print(key)
        print(players_games[key])

if __name__ == '__main__':
    test()
