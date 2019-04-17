def write_and_erase(N: int, A: list)->int:
    d = {}
    for a in A:
        d.setdefault(a, 0)
        d[a] = (d[a] + 1) % 2

    return sum(v for v in d.values())


if __name__ == "__main__":
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = write_and_erase(N, A)
    print(ans)
