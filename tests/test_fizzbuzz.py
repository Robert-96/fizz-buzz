from app.fizzbuzz import *

import pytest


@pytest.mark.parametrize(
    "divisor, number, response",
    [
        (3, 3, True),
        (3, 6, True),
        (3, 9, True),
        (5, 5, True),
        (5, 10, True),
        (5, 15, True),
        (3, 1, False),
        (3, 2, False),
        (3, 4, False),
        (3, 5, False),
        (5, 1, False),
        (5, 2, False),
        (5, 3, False),
        (5, 4, False),
        (5, 6, False)
    ]
)
def test_divisible_by(divisor, number, response):
    assert divisible_by(divisor, number) == response


@pytest.mark.parametrize(
    "number, response",
    [
        (3, True),
        (6, True),
        (9, True),
        (1, False),
        (2, False),
        (4, False)
    ]
)
def test_divisible_by_three(number, response):
    assert divisible_by_three(number) == response


@pytest.mark.parametrize(
    "number, response",
    [
        (5, True),
        (10, True),
        (15, True),
        (1, False),
        (2, False),
        (3, False),
        (4, False),
        (6, False)
    ]
)
def test_divisible_by_five(number, response):
    assert divisible_by_five(number) == response


@pytest.mark.parametrize(
    "number, response",
    [
        (15, True),
        (30, True),
        (45, True),
        (3, False),
        (5, False),
        (10, False)
    ]
)
def test_divisible_by_fifteen(number, response):
    assert divisible_by_fifteen(number) == response


class TestFizzBuzz(object):

    @pytest.mark.parametrize(
        "number, response",
        [
            (1, "1"),
            (2, "2"),
            (3, "Fizz"),
            (4, "4"),
            (5, "Buzz"),
            (6, "Fizz"),
            (7, "7"),
            (8, "8"),
            (9, "Fizz"),
            (10, "Buzz"),
            (11, "11"),
            (12, "Fizz"),
            (13, "13"),
            (14, "14"),
            (15, "Fizz-Buzz"),
        ]
    )
    def test_get(self, number, response):
        assert FizzBuzz.get(number) == response


    def test_play(self, capsys):
        FizzBuzz.play(5)

        captured = capsys.readouterr()
        assert captured.out == "1\n2\nFizz\n4\nBuzz\n"