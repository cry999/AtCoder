def all_your_paths_are_different_lengths(L: int)->tuple:
    if L == 1:
        return 2, [(1, 2, 0)]

    r = 0
    while 2 ** (r+1) <= L:
        r = r + 1

    N = r + 1
    edges = []
    power2 = 1
    for i in range(1, N):
        edges.append((i, i+1, 0))
        edges.append((i, i+1, power2))
        power2 = power2 * 2

    for t in range(N-1, 0, -1):
        if L - (2**(t-1)) >= 2**r:
            edges.append((t, N, L - 2**(t-1)))
            L = L - 2**(t-1)

    return N, edges


if __name__ == "__main__":
    L = int(input())
    N, edges = all_your_paths_are_different_lengths(L)
    print(N, len(edges))
    for u, v, w in edges:
        print(u, v, w)
