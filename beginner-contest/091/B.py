def two_color_card_games(N: int, S: list, M: int, T: list) -> int:
    # default おこずかいを失う言葉しかない場合は、何も言わない。
    d = {'': 0}
    for s in S:
        d.setdefault(s, 0)
        d[s] += 1

    for t in T:
        d.setdefault(t, 0)
        d[t] -= 1

    return max(d.values())


if __name__ == "__main__":
    N = int(input())
    S = [input() for _ in range(N)]
    M = int(input())
    T = [input() for _ in range(M)]
    ans = two_color_card_games(N, S, M, T)
    print(ans)
