from src.checkSudoku import checkSudoku
import pytest

@pytest.mark.irregular
def test_irregular():
    
    irregular = [[1,2,3],
             [2,3,1]]

    irregular2 = [[1,2,3],
             [2,3,1],
             [3,1]]