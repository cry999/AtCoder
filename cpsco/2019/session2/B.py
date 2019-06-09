def telephoneQ(N: int, queries: list)->int:
    plus = 0
    mul = 1

    for c, a in queries:
        if c == '+':
            plus += a
        elif c == '*':
            mul *= a if a != 0 else 1

    return plus * mul


if __name__ == "__main__":
    N = int(input())
    queries = []
    for _ in range(N):
        c, a = input().split()
        queries.append((c, int(a)))

    ans = telephoneQ(N, queries)
    print(ans)
