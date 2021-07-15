#!python3

"""
     "Виселица"
"""

from game_gallow import GameGallow, StateGame
def main():
    game = GameGallow()
    while game.state==StateGame.continues:
        input_letter = input(
            f'Enter a letter in word <{game.word_unknown}> pls : ').lower()
        result = game.trying_guess(input_letter)
        print(result, game.state.name)
    

__author__ = "Aliaksandr Babtsou"
__copyright__ = "Copyright 2021, The Summer Bootcamp"


if __name__ == '__main__':
    main()