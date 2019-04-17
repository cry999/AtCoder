class CumulativeSum2D:
    """2次元累積和クラス
    """

    def __init__(self, size: int):
        self.size = size
        self.data = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    def add(self, l: int, r: int, v: int):
        """(l, r) に v を加える
        """
        self.data[l][r] += v

    def build(self):
        """2次元累積和を構築する
        """
        for l in range(self.size):
            for r in range(self.size):
                self.data[l + 1][r + 1] += self.data[l + 1][r]
                self.data[l + 1][r + 1] += self.data[l][r + 1]
                self.data[l + 1][r + 1] += -self.data[l][r]

    def query(self, l: int, r: int) -> int:
        """(l, r] x (l, r] の範囲をクエリする
        """
        return self.data[r][r] + self.data[l][l] - self.data[l][r] - self.data[r][l]


def atcoder_express2(
        N: int, M: int, Q: int, data: list, queries: list) -> list:
    # 二次元累積和
    S = CumulativeSum2D(N)
    for l, r in data:
        S.add(l, r, 1)
    S.build()

    return [S.query(p-1, q) for p, q in queries]


if __name__ == "__main__":
    M, Q = 0, 0
    N, M, Q = map(int, input().split())
    data = [tuple(int(s) for s in input().split()) for _ in range(M)]
    queries = [tuple(int(s) for s in input().split()) for _ in range(Q)]
    ans = atcoder_express2(N, M, Q, data, queries)
    for a in ans:
        print(a)
