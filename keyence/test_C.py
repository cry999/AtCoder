import unittest
from . import C


class TestC(unittest.TestCase):

    def test_exam_and_wizard(self):
        """test of C.exam_and_wizard
        """
        t = [
            (
                [2, 3, 5],
                [3, 4, 1],
                3,
            ),
            (
                [2, 3, 3],
                [2, 2, 1],
                0,
            ),
            (
                [17, 7, 1],
                [25, 6, 14],
                -1,
            ),
            (
                [757232153, 372327760, 440075441, 195848680, 354974235, 458054863,
                    463477172, 740174259, 615762794, 632963102, 529866931, 64991604, ],
                [74164189, 98239366, 465611891, 362739947, 147060907, 118867039,
                    63189252, 78303147, 501410831, 110823640, 122948912, 572905212, ],
                5,
            ),
        ]
        for a, b, expected in t:
            with self.subTest(a=a, b=b):
                actual = C.exam_and_wizard(a, b)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
