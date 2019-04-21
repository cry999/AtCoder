def generate_rects(N: int)->list:
    for x1 in range(N):
        for y1 in range(N):
            for x2 in range(x1, N):
                for y2 in range(y1, N):
                    yield x1, y1, x2, y2


def gold_game(W: int, H: int, N: int, machines: list)->int:
    memo = {}

    def dfs(sx: int, sy: int, tx: int, ty: int)->int:
        if (sx, sy, tx, ty) in memo:
            return memo[(sx, sy, tx, ty)]

        max_gold = 0
        for mx, my in machines:
            if mx < sx or tx <= mx:
                continue
            if my < sy or ty <= my:
                continue

            gold = (tx-sx) + (ty-sy) - 1
            gold += dfs(sx, sy, mx, my)      # 左下
            gold += dfs(sx, my+1, mx, ty)    # 左上
            gold += dfs(mx+1, sy, tx, my)    # 右下
            gold += dfs(mx+1, my+1, tx, ty)  # 右上

            max_gold = max(max_gold, gold)

        memo[(sx, sy, tx, ty)] = max_gold
        return max_gold

    return dfs(1, 1, W+1, H+1)


if __name__ == "__main__":
    W, H = map(int, input().split())
    N = int(input())
    machines = [tuple(int(s) for s in input().split()) for _ in range(N)]

    ans = gold_game(W, H, N, machines)
    print(ans)
