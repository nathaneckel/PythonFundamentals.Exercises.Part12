from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    return [i for i in range(start, stop) if i % 2 != parity.value]

#RETURN     [  ACTION     ITERATE    (for)     CONDITION (if) ]

# DO   FOR    IF
# NOT  FOR    IF      DO  (like normally)

"""
Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
updating this here docstring to something useful.

:param start:
    :param stop:
    :param parity:
    :return:
    """

def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    return {i:strategy(i) for i in range(start, stop)}


"""
Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    #pass


def gen_set(val_in: str) -> Set:
    return set([letter.upper() for letter in val_in if letter.islower()])

#    return {i:strategy(i) for i in range(start, stop)}
#     return [i for i in range(start, stop) if i % 2 != parity.value]
"""
THIS IS ALL ABOUT CAPS / lowers / Title / camelCase
Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
updating this here docstring to something useful.

    :param val_in:
    :return:
    """
