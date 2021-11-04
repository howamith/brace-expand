# Project modules.
from brace_expand import brace_expand

# PyPi modules.
from ddt import data, ddt

# Standard libary modules.
from typing import List, Tuple
from unittest import TestCase


@ddt
class BraceExpandTests(TestCase):
    """brace-expand tests."""

    @data(
        (
            # Test nested expansion.
            "{hello,goodbye} {world,my {friends,colleagues}}",
            [
                "hello world",
                "goodbye world",
                "hello my friends",
                "hello my colleagues",
                "goodbye my friends",
                "goodbye my colleagues",
            ],
        ),
        (
            # Test range.
            "1..9",
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ),
        (
            # Test nested range (note that in bash "192.169.1.2" would be at the
            # end - our implemenation should be fixed to replicate this).
            "192.{168.{1..9}.2,169.1.2}",
            [
                "192.169.1.2",
                "192.168.1.2",
                "192.168.2.2",
                "192.168.3.2",
                "192.168.4.2",
                "192.168.5.2",
                "192.168.6.2",
                "192.168.7.2",
                "192.168.8.2",
                "192.168.9.2",
            ],
        ),
        (
            # Nested ranges and coma-separated lists.
            "python{2.{5..7},3.{6,8,9}}",
            [
                "python2.5",
                "python2.6",
                "python2.7",
                "python3.6",
                "python3.8",
                "python3.9",
            ],
        ),
        (
            # Ignore ranges in non-numeric expressions.
            "hello..world",
            ["hello..world"],
        ),
        # Test that unbalanced expressions don't cause us to fall over.
        (
            "{hello,goodbye} {world,my {friends,colleagues}",
            [
                "hello {world,my {friends,colleagues}",
                "goodbye {world,my {friends,colleagues}",
            ],
        ),
    )
    def test_it_works(self, value: Tuple[str, List[str]]) -> None:
        """Perform tests that verify that brace-expand works.

        Args:
            value: A Tuple of input strings, and their expected result when run
              through brace_expand.
        """

        input, expected = value
        result = brace_expand(input)
        self.assertEqual(result, expected)
