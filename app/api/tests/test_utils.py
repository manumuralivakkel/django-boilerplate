import pytest
from api.utils import *

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
def test_subtract():
    assert subtract(5,2) == 3
   