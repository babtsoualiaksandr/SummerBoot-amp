import pytest
from game_gallow import GameGallow
from game_gallow import StateGame


@pytest.fixture
def greate_game():
   return GameGallow()

@pytest.fixture
def input_value_no_letter():
   input = '3'
   return input

def input_value_letter():
   input = 'q'
   return input


def test_init_game():
    game = GameGallow()
    assert game.state==StateGame.continues

def test_input_no_letter(greate_game, input_value_no_letter):
    error = "Error input" in greate_game.trying_guess(input_value_no_letter)
    assert error==True

def test_input_letter(greate_game, input_value_letter):

    assert "Error input" in greate_game.trying_guess(input_value_letter)==True

