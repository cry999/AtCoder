def liar_takahashi(N: int, a: int, b: int, K: int, P: list) -> bool:
    visited = set([a, b])
    for p in P:
        if p in visited:
            return False
        visited.add(p)
    return True


if __name__ == "__main__":
    N = int(input())
    a, b = map(int, input().split())
    K = int(input())
    P = [int(s) for s in input().split()]

    yes = liar_takahashi(N, a, b, K, P)
    print('YES' if yes else 'NO')
