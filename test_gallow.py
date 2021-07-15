import pytest
from game_gallow import GameGallow
from game_gallow import StateGame, letter_from_player


@pytest.fixture
def greate_game():
    return GameGallow()


@pytest.fixture
def input_value_no_letter():
    input = '3'
    return input


@pytest.fixture
def input_value_two_letter():
    input = 'qq'
    return input


def test_init_game():
    game = GameGallow()
    assert game.state == StateGame.continues


def test_input_no_letter(greate_game, input_value_no_letter):
    error = "Error input" in greate_game.trying_guess(input_value_no_letter)
    assert error == True


def test_input_two_letter(greate_game, input_value_two_letter):
    error = "Error input" in greate_game.trying_guess(input_value_two_letter)
    assert error == True

def test_letter_from_user(greate_game):
    players_games={}
    game = greate_game
    letter_from_player('007','01',players_games) 
    if '007' in players_games:
       return True
    else:
       False


