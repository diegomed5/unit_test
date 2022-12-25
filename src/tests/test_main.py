import pytest
from src.main import sum, is_greater_than, login

def test_sum():
    assert sum(2,5) == 7

def test_is_greater_than():
    assert is_greater_than(10, 5)


@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (7,1,8),
        (6,sum(4,2),12),
        (sum(19,1),15,35),
        (-16,10,sum(-16,10))
    ]
)
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x, input_y) == expected


def test_login_pass():
    login_passes=login("diegomed5", "271019")
    assert login_passes

def test_login_fail():
    login_fails=login("diegomed55", "1271019")
    assert not login_fails