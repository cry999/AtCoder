import math


def mod_pow(a: int, n: int, mod: int)->int:
    ret = 1
    for _ in range(n):
        ret = (ret * a) % mod
    return ret


def lining_up(N: int, A: list)->int:
    pos = [0] * math.ceil(N / 2)

    for a in A:
        i = (N-a-1)//2
        pos[i] += 1

        if pos[i] > 2:
            return 0

    if N % 2 == 0 and any(p != 2 for p in pos):
        return 0
    if N % 2 == 1 and any(p != 2 for p in pos[:-1]) and pos[-1] != 1:
        return 0

    return mod_pow(2, N // 2, 10**9+7)


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = lining_up(N, A)
    print(ans)
