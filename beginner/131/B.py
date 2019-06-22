def bite_eating(N: int, L: int)->int:
    total = N*(N-1)//2 + L*N

    if L >= 0:
        # L が正の値なら一番小さいものを食べる。
        return total-L

    if N+L-1 < 0:
        # L が負の値かつ一番大きい値も負であるなら一番大きいものを食べる。
        return total-(N+L-1)

    # 上述の条件に当てはまらない場合は、必ず美味しさ 0
    # のものが存在するのでそれを食べる。
    return total


if __name__ == "__main__":
    N, L = map(int, input().split())

    ans = bite_eating(N, L)
    print(ans)
