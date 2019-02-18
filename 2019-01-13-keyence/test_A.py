import unittest
from . import A


class TestA(unittest.TestCase):
    """test class of A
    """

    def test_is1974(self):
        """ test for is1974
        """
        t = [
            (1, 7, 9, 4, True),
            (1, 9, 7, 4, True),
            (1, 2, 9, 1, False),
            (4, 9, 0, 8, False),
        ]
        for n1, n2, n3, n4, expected in t:
            with self.subTest(n1=n1, n2=n2, n3=n3, n4=n4):
                actual = A.is1974(n1, n2, n3, n4)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
