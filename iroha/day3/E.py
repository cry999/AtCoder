def ku(N: int, C: list) -> int:
    i = 0
    count = 0

    while i < N:
        l = 0
        while i < N and C[i] == '/':
            l += 1
            i += 1

        r = 0
        while i < N and C[i] == '\\':
            r += 1
            i += 1

        count += 1 if r == l else 0

    return count


if __name__ == "__main__":
    N = int(input())
    C = [input() for _ in range(N)]

    ans = ku(N, C)
    print(ans)
