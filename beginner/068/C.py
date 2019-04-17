def cat_snuke_and_a_voyage(N: int, M: int, ships: list)->bool:
    passable = [(False, False)] * (N-2)
    for a, b in ships:
        if a == 1:
            _, bN = passable[b-2]
            passable[b-2] = (True, bN)
            if bN:
                return True
        elif b == N:
            a1, _ = passable[a-2]
            passable[a-2] = (a1, True)
            if a1:
                return True
    return False


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    ships = [tuple(map(int, input().split())) for _ in range(M)]
    yes = cat_snuke_and_a_voyage(N, M, ships)
    print('POSSIBLE' if yes else 'IMPOSSIBLE')
