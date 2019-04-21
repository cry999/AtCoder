def eat_takoyaki(N: int, T: list)->int:
    return sorted(T)[0]


if __name__ == "__main__":
    N = int(input())
    T = [int(input()) for _ in range(N)]

    ans = eat_takoyaki(N, T)
    print(ans)
