import unittest
from . import B


class TestB(unittest.TestCase):
    """test for B
    """

    def test_keyence_string(self):
        """test of B.keyence_string
        """
        t = [
            ('keyofscience', True),
            ('mpyszsbznf', False),
            ('ashlfyha', False),
            ('keyence', True),
        ]
        for s, expected in t:
            with self.subTest(s=s):
                actual = B.keyence_string(s)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
