class SegmentTree:
    def __init__(self, size: int):
        self.size = 1
        while self.size < size:
            self.size <<= 1
        self.data = [0] * (2*self.size-1)

    def update(self, idx: int, val: int):
        idx += self.size-1
        self.data[idx] = val

        while idx > 0:
            idx = (idx-1)//2
            self.data[idx] = self.data[2*idx+1] | self.data[2*idx+2]

    def get(self, idx: int)->int:
        return self.data[idx+self.size-1]

    def query(self, a: int, b: int)->int:
        return self.__query(a, b, 0, 0, self.size)

    def __query(self, a: int, b: int, k: int, l: int, r: int)->int:
        if r <= a or b <= l:
            return 0
        if a <= l and r <= b:
            return self.data[k]
        vl = self.__query(a, b, 2*k+1, l, (l+r)//2)
        vr = self.__query(a, b, 2*k+2, (l+r)//2, r)
        return vl | vr


def check(x: int, K: int, N: int, st: SegmentTree)->bool:
    res = 0
    r = 0
    for l in range(N):
        while r < N and st.query(l, r+1) < x:
            r += 1
        res += N-r
    return res >= K


def or_problem(N: int, K: int, A: list)->int:
    st = SegmentTree(N)

    for i, a in enumerate(A):
        st.update(i, a)

    l, r = 0, 1 << 60
    while r-l > 1:
        m = (l+r)//2

        if check(m, K, N, st):
            l = m
        else:
            r = m

    return l


if __name__ == "__main__":
    N = 0
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    ans = or_problem(N, K, A)
    print(ans)
