def factions(N: int, M: int, relations: list) -> int:
    d = [[False] * N for _ in range(N)]

    for x, y in relations:
        d[x - 1][y - 1] = True
        d[y - 1][x - 1] = True

    def is_clique(vertexes: list) -> bool:
        for i, v in enumerate(vertexes):
            for u in vertexes[i + 1:]:
                if not d[u][v]:
                    # 繋がっていない 2 頂点があればクリークでない
                    return False
        return True

    # 全探索
    max_num = 0
    for S in range(1 << N):
        vertexes = []
        for i in range(N):
            if S & (1 << i):
                vertexes.append(i)

        if is_clique(vertexes):
            max_num = max(max_num, len(vertexes))

    return max_num


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    relations = [tuple(int(s) for s in input().split()) for _ in range(M)]

    ans = factions(N, M, relations)
    print(ans)
