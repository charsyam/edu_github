import pytest

from src.add import minus


def test_minus_true():
	assert add(1, 2) == -1
	assert add(2, 3) == -1
	assert add(3, 3) == 0

def test_minus_false():
	assert add(4, 4) != 2
