import unittest
from . import D


class TestD(unittest.TestCase):

    def test_is_unique(self):
        t = [
            ([1, 2, 3], True),
            ([1, 2, 1], False),
        ]
        for l, expected in t:
            with self.subTest(l=l):
                actual = D.is_unique(l)
                self.assertEqual(expected, actual)

    def test_double_landscape(self):
        t = [
            (
                2, 2,
                [4, 3],
                [3, 4],
                2,
            ),
            (
                3, 3,
                [5, 9, 7],
                [3, 6, 9],
                0,
            ),
            (
                2, 2,
                [4, 4],
                [4, 4],
                0,
            ),
            (
                14, 13,
                [158, 167, 181, 147, 178, 151, 179,
                    182, 176, 169, 180, 129, 175, 168],
                [181, 150, 178, 179, 167, 180, 176, 169, 182, 177, 175, 159, 173],
                343772227,
            ),
        ]

        for N, M, A, B, expected in t:
            with self.subTest(N=N, M=M, A=A, B=B):
                actual = D.double_landscape(N, M, A, B)
                self.assertEqual(expected, actual)
