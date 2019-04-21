import queue


def maze_bfs(R: int, C: int, s: tuple, g: tuple, maze: list)->int:
    sr, sc = s
    sr, sc = sr-1, sc-1

    gr, gc = g
    gr, gc = gr-1, gc-1

    q = queue.Queue()
    q.put((sr, sc))

    route = [[float('inf')] * C for _ in range(R)]
    route[sr][sc] = 0

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while not q.empty():
        r, c = q.get()

        for dr, dc in dirs:
            if r+dr < 0 or R <= r+dr:
                # out of range
                continue
            if c+dc < 0 or C <= c+dc:
                # out of range
                continue

            if maze[r+dr][c+dc] == '#':
                # wall
                continue

            if route[r][c]+1 < route[r+dr][c+dc]:
                # can update
                route[r+dr][c+dc] = route[r][c]+1
                q.put((r+dr, c+dc))

    return route[gr][gc]


if __name__ == "__main__":
    R = 0
    R, C = map(int, input().split())
    sr, sc = map(int, input().split())
    gr, gc = map(int, input().split())
    maze = [input() for _ in range(R)]

    ans = maze_bfs(R, C, (sr, sc), (gr, gc), maze)
    print(ans)
