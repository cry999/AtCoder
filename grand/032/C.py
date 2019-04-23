def has_circuit(g: list, s: int, ng: int) -> bool:
    stack = []
    stack.append((s, -1))  # (現在の頂点, 親)

    while len(stack) > 0:
        u, p = stack.pop()

        if u == s and p >= 0:
            return True

        for v in g[u]:
            if v == ng:
                continue
            if v == p:
                continue
            stack.append((v, u))
    return False


def three_circuit(N: int, M: int, edges: list) -> bool:
    g = [[] for _ in range(N)]

    for u, v in edges:
        g[u-1].append(v-1)
        g[v-1].append(u-1)

    dims = [len(p) for p in g]

    if not all(d % 2 == 0 for d in dims):
        # オイラー閉路でない
        return False

    if max(dims) >= 6:
        # 次元数が 6 以上の頂点があるならそいつを利用して
        # 3 つのサーキットが作れる。
        return True

    # 次元数 4 の頂点集合
    vertexes = [v for v in range(N) if dims[v] == 4]

    if len(vertexes) >= 3:
        # 次元数 4 の頂点が 3 つ以上存在するなら OK
        return True

    if len(vertexes) == 2:
        # 次元数 4 の頂点が 2 つのみ存在する場合、ありうるのは、この
        # 2 頂点の間にパスが 4 つある場合と 2 つある場合。
        # 前者は図を書けばすぐわかるが高々 2 つのサーキットしか作れな
        # い。後者の場合は、この 2 頂点を含むサーキットが 1 つとそれ
        # ぞれの頂点しか含まないサーキットが 1 つずつ、計 3 つ作れる。

        # 次数 4 の頂点からスタートしてほかの次数 4 の頂点に出会わずに
        # 帰ってこれるパスが存在すれば次数 4 の頂点間にはパスがちょうど
        # 2 つとなる。
        return has_circuit(g, vertexes[0], vertexes[1])
    # 残りは 次数 4 の点が 1 つ、あるいはすべての頂点の次数が 2 となる。
    # 前者の場合、高々 2 つのサーキット、後者の場合は高々 1 つのサーキッ
    # トしか作れないのは自明。
    return False


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    edges = [tuple(int(s) for s in input().split()) for _ in range(M)]

    yes = three_circuit(N, M, edges)
    print('Yes' if yes else 'No')
