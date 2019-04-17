from math import ceil


def widespread(N: int, A: int, B: int, H: list)->int:
    def killable_by(T: int)->bool:
        return sum(max(0, ceil((h-B*T)/(A-B))) for h in H) <= T

    l, r = 0, 10**9
    while r - l > 1:
        m = (l + r) // 2
        if killable_by(m):
            r = m
        else:
            l = m

    return r


if __name__ == "__main__":
    N = 0
    N, A, B = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    ans = widespread(N, A, B, H)
    print(ans)
