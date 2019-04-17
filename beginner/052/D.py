def walk_and_teleport(N: int, A: int, B: int, X: list)->int:
    pos = X[0]
    cost = 0

    for x in X[1:]:
        cost += min(A * (x - pos), B)
        pos = x

    return cost


if __name__ == "__main__":
    N, A, B = map(int, input().split())
    X = [int(s) for s in input().split()]
    ans = walk_and_teleport(N, A, B, X)
    print(ans)
