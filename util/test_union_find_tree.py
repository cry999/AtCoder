import unittest
from .union_find_tree import UnionFindTree


class TestUnionFindTree(unittest.TestCase):

    def test_union_find_tree(self):
        uft = self.__default_uft()

        self.assertTrue(uft.same(0, 1))
        self.assertTrue(uft.same(2, 4))
        self.assertTrue(uft.same(2, 3))

        self.assertFalse(uft.same(0, 2))

    def __default_uft(self) -> UnionFindTree:
        uft = UnionFindTree(5)

        uft.summarize(0, 1)
        uft.summarize(2, 3)
        uft.summarize(3, 4)

        return uft


if __name__ == "__main__":
    unittest.main()
