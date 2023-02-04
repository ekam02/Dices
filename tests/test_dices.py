from dices import *


class TestDices:
    def test_dices(self):
        a = Dices(5)
        assert len(a.dice_list) == 5

    def test_set_dices(self):
        a = Dices(5)
        a.dice_list = [5]
        assert a.dice_list[0] == 5
        a.dice_list = [3, 6]
        assert a.dice_list == [3, 6]
