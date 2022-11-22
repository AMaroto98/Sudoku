from src.checkSudoku import checkSudoku
import pytest


def test_incorrect():

    incorrect = [[1,2,3,4],
                [2,3,1,3],
                [3,1,2,3],
                [4,4,4,2]]

    incorrect2 = [[1,2,3,4],
                [2,3,1,2],
                [4,1,2,3],
                [2,3,1,4]]

    incorrect3 = [[1,2,3,4,5],
                [2,3,1,5,6],
                [4,5,2,1,3],
                [3,4,5,2,1],
                [5,6,4,3,2]]

    incorrect4 = [['a','b','c'],
                ['b','c','a'],
                ['c','a','b']]

    incorrect5 = [ [1, 1.5],
                [1.5, 1]]