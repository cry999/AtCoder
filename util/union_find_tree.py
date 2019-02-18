class UnionFindTree:

    def __init__(self, size: int):
        """UnionFindTreeを初期化します
        :param size: サイズ
        :return: UnionFindTree
        """
        if size < 0:
            raise Exception('size must be greater than 0.')

        self.__parent = [-1] * size

    def summarize(self, a: int, b: int):
        """aを含む木とbを含む木をまとめます
        :param a: 木a
        :param b: 木b
        """
        a = self.__root(a)
        b = self.__root(b)

        if a != b:
            self.__parent[b] = a

    def __root(self, a: int) -> int:
        """aの根を求めます
        :param a: 木の要素
        :return: 根
        """
        if self.__parent[a] == -1:
            return a
        else:
            return self.__root(self.__parent[a])

    def same(self, a: int, b: int) -> bool:
        """a と b が同じ木に属するかを判断します
        :param a: 木
        :param b: 木
        :return: a と b が同じ木なら True。そうでないなら False。
        """
        return self.__root(a) == self.__root(b)
