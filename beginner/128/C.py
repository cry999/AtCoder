def switches(N: int, M: int, sw: list, P: list)->int:
    count = 1 << N
    sw_state = [0] * N
    li_state = [0] * M
    for i in range(1 << N):
        for j in range(N):
            sw_state[j] = 1 if (i & 1) != 0 else 0
            i >>= 1

        for m in range(M):
            li_state[m] = 0
            for si in sw[m][1:]:
                li_state[m] += sw_state[si-1]

            if li_state[m] % 2 != P[m]:
                break
        else:
            continue

        count -= 1

    return count


if __name__ == "__main__":
    M = 0

    N, M = map(int, input().split())
    sw = [[int(s) for s in input().split()] for _ in range(M)]
    P = [int(s) for s in input().split()]

    ans = switches(N, M, sw, P)
    print(ans)
