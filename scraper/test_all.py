import pytest

from main import *

def test_GameNotation():
    chess = GameNotation('name')
    assert chess.game_nr == 0
    assert chess.variant == 0


def test_MoveNotation():
    chess = MoveNotation('name')
    sectors = ['name','name']
    assert chess.move == sectors[0]
    assert chess.date == sectors[0]
    assert chess.clock== sectors[1]
    assert sectors.line == split("]")
