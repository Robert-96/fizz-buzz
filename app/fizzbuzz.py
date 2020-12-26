"""Fizz-Buzz is a group word game for children to teach them about division.

>>> FizzBuzz.play(5)
1
2
Fizz
4
Buzz

"""


def divisible_by(divisor, number):
    """Return True if the ``number`` is divisible by ``divisor``.

    >>> divisible_by(3, 6)
    True

    >>> divisible_by(5, 10)
    True

    >>> divisible_by(3, 4)
    False
    """

    return number % divisor == 0


def divisible_by_three(number):
    """Return True if the ``number`` is divisible by 3.

    >>> divisible_by_three(6)
    True

    >>> divisible_by_three(9)
    True

    >>> divisible_by_three(4)
    False
    """

    return divisible_by(3, number)


def divisible_by_five(number):
    """Return True if the ``number`` is divisible by 5.

    >>> divisible_by_five(10)
    True

    >>> divisible_by_five(15)
    True

    >>> divisible_by_five(6)
    False
    """

    return divisible_by(5, number)


def divisible_by_fifteen(number):
    """Return True if the ``number`` is divisible by 15.

    >>> divisible_by_fifteen(15)
    True

    >>> divisible_by_fifteen(30)
    True

    >>> divisible_by_fifteen(16)
    False
    """

    return divisible_by(15, number)


class FizzBuzz(object):

    @classmethod
    def get(cls, number):
        """Return the word ``Fizz`` for numbers divisible by three, for any number divisible by
        five return the word ``Buzz``, and for numbers divisible by 15 return ``Fizz-Buzz``.

        >>> FizzBuzz.get(1)
        '1'

        >>> FizzBuzz.get(3)
        'Fizz'

        >>> FizzBuzz.get(5)
        'Buzz'

        >>> FizzBuzz.get(15)
        'Fizz-Buzz'
        """

        if divisible_by_fifteen(number):
            return "Fizz-Buzz"
        if divisible_by_three(number):
            return "Fizz"
        if divisible_by_five(number):
            return "Buzz"
        else:
            return str(number)

    @classmethod
    def play(cls, limit=100):
        """Plays Fizz-Buzz."""

        if limit > 0:
            cls.play(limit - 1)
            print(cls.get(limit))


if __name__ == "__main__":
    FizzBuzz.play(100)
