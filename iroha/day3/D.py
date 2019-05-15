def onigokko(N: int, S: list):
    dirs = [('U', -1, 0), ('R', 0, 1), ('L', 0, -1), ('D', 1, 0)]

    me = (1, 1)
    iroha = (N-2, N-2)

    while True:
        c = '-'
        if abs(me[0]-iroha[0]) + abs(me[1]-iroha[1]) == 1:
            c = '-'
            for _c, dr, dc in dirs:
                nr, nc = me[0]+dr, me[1]+dc
                if S[nr][nc] == '.' and (nr, nc) != iroha:
                    c, me = _c, (nr, nc)
                    break

        print(c, flush=True)

        x, y = map(int, input().split())
        if (x, y) == (-2, -2):
            raise Exception('caught')
        elif (x, y) == (-3, -3):
            return
        elif (x, y) != (-1, -1):
            iroha = (x-1, y-1)


if __name__ == "__main__":
    N = int(input())
    S = [input() for _ in range(N)]

    onigokko(N, S)
