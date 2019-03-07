class BIT:
    """1-indexed BIT
    """

    def __init__(self, size: int):
        """サイズを指定して BIT を初期化します。
        """
        # BIT のサイズは 2^n + 1
        self.__size = 1
        while self.__size < size:
            self.__size *= 2
        self.__size += 1

        # 実際の配列
        self.__bit = [0] * self.__size

    def add(self, idx: int, val: int):
        """位置 idx (1-indexed) に値 val をたす。
        :param idx: 値を追加したいインデックス
        :param val: 追加したい値
        """
        while idx < self.__size:
            self.__bit[idx] += val
            idx += idx & (-idx)

    def sum(self, l: int, r: int)->int:
        """(l, r] の累積和を計算する。
        :param l: left index
        :param r: right index
        :return: (l, r] の累積和
        """
        return self.__sum__(r) - self.__sum__(l)

    def __sum__(self, idx: int)->int:
        s = 0
        while idx > 0:
            s += self.__bit[idx]
            idx -= idx & (-idx)
        return s


def convert(A: list)->list:
    B = sorted(A)
    C = []
    N = len(A)
    for a in A:
        l, r = 0, N
        while 1 < r - l:
            m = (l+r)//2
            if a < B[m]:
                r = m
            else:
                l = m
        C.append(r)
    return C


def inversion(A: list)->int:
    n = len(A)
    _A = convert(A)
    bit = BIT(n)
    s = 0
    for j, a in enumerate(_A):
        s += j - bit.sum(0, a)
        bit.add(a, 1)
    return s


def check(A: list, x: int)->int:
    # n = len(A)
    # bit = BIT(n)
    # for i, a in enumerate(A):
    #     bit.add(i+1, 1 if a >= x else -1)

    s = 0
    B = []
    for a in A:
        s += 1 if a >= x else -1
        B.append(s)
    return inversion(B)
    # return inversion([bit.sum(0, i+1) for i in range(n)])


def median_of_medians(N: int, A: list)->int:
    alpha = sorted(A)
    l, r = 0, N
    m, c = N//2, N*(N+1)//2
    while True:
        if check(A, alpha[m]) <= c//2:
            if m == N-1:
                break
            elif check(A, alpha[m+1]) > c//2:
                break
            else:
                l, m = m, (m+r)//2
        else:
            m, r = (m+l)//2, m+1

    return alpha[m]


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    ans = median_of_medians(N, A)
    print(ans)
