from random import Random
from format import FORMAT


class Dices:
    def __init__(self, cant: int) -> None:
        if cant > 0:
            self.__dice_list = Random().choices(range(1, 7), k=cant)
        else:
            raise

    @property
    def dice_list(self) -> list:
        return self.__dice_list

    @dice_list.setter
    def dice_list(self, d_list: list):
        if isinstance(d_list, list):
            self.__dice_list = d_list
        elif isinstance(d_list, tuple):
            self.__dice_list = list(d_list)
        else:
            raise

    def __str__(self) -> str:
        dices = FORMAT[0]*len(self.__dice_list)
        for i in range(3):
            dices += '\n'
            for j in self.dice_list:
                dices += FORMAT[j][i]
        dices += f'\n{FORMAT[7]*len(self.__dice_list)}'
        return dices


if __name__ == '__main__':
    a = Dices(5)
    print(a.dice_list)
    z = Random().choices(range(1, 7), k=7)
    a.dice_list = z
    print(a.dice_list)
    print(a)
