def vote(N: int, S: list)->int:
    d = {}
    for s in S:
        d.setdefault(s, 0)
        d[s] += 1

    return sorted(d.items(), key=lambda x: -x[1])[0][0]


if __name__ == "__main__":
    N = int(input())
    S = [input() for _ in range(N)]
    ans = vote(N, S)
    print(ans)
