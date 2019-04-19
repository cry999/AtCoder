def amida(N: int, M: int, D: int, A: list)->list:
    to2from = {i+1: i+1 for i in range(N)}

    for a in A:
        i, j = a, a+1
        to2from[i], to2from[j] = to2from[j], to2from[i]

    from2to = [{_from: to for to, _from in to2from.items()}]

    k = 0
    while (1 << k) <= D:
        k += 1
        f2t = from2to[-1]
        from2to.append({i+1: f2t[f2t[i+1]] for i in range(N)})

    # この時点で from2to[k][i] は 2^k 個のあみだを縦に連結した時の
    # i の出口となる。
    # あとは、D を 2 進数で表記して必要な k を特定しながら計算すること
    # これで全体で O(N logD) になるはず
    res = [i+1 for i in range(N)]
    k = 0
    while (1 << k) <= D:
        if D & (1 << k) != 0:
            for i in range(N):
                res[i] = from2to[k][res[i]]
        k += 1

    return res


if __name__ == "__main__":
    N, M, D = map(int, input().split())
    A = [int(s) for s in input().split()]

    ans = amida(N, M, D, A)
    for a in ans:
        print(a)
