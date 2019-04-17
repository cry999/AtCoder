def coloring_dominoes(N: int, S1: str, S2: str)->int:
    MOD = 1000000007

    if S1[0] == S2[0]:
        offset = 1
        ret = 3
        before_dir = S1[0] == S2[0]
    else:
        offset = 2
        ret = 3 * 2
        before_dir = S1[0] == S2[0]

    i = offset
    while i < N:
        current_dir = S1[i] == S2[i]

        if before_dir and current_dir:
            ret *= 2
            i += 1
        elif before_dir and not current_dir:
            ret *= 2 * 1
            i += 2
        elif not before_dir and current_dir:
            ret *= 1
            i += 1
        else:
            ret *= 3
            i += 2

        ret %= MOD
        before_dir = current_dir

    return ret


if __name__ == "__main__":
    N = int(input())
    S1 = input()
    S2 = input()
    ans = coloring_dominoes(N, S1, S2)
    print(ans)
