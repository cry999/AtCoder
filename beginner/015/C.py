def found_bug(N: int, K: int, T: list)->bool:
    def rec(n: int)->list:
        if n == N:
            return [0]

        ret = []
        for k in range(K):
            ret += [T[n][k] ^ a for a in rec(n+1)]
        return ret

    return any(a == 0 for a in rec(0))


if __name__ == "__main__":
    N = 0
    N, K = map(int, input().split())
    T = [[int(s) for s in input().split()] for _ in range(N)]

    yes = found_bug(N, K, T)
    print('Found' if yes else 'Nothing')
