from question3 import get_password
import pytest

# Test  password length
def test_low_password_length():
    password = get_password(6)
    assert len(password) == 6
def test_medium_password_length():
    password = get_password(9)
    assert len(password) == 9
def test_hard_password_length():
    password = get_password(11)
    assert len(password) == 11
def test_very_hard_password_length():
    password =get_password(12)
    assert len(password) == 12

if __name__ == '__main__':
     pytest.main()