def traveling(N: int, plan: list)->bool:
    ct, cx, cy = 0, 0, 0
    for nt, nx, ny in plan:
        if nt-ct < abs(nx-cx) + abs(ny-cy):
            return False
        if (nt-ct) % 2 != (abs(nx-cx) + abs(ny-cy)) % 2:
            return False
    return True


if __name__ == "__main__":
    N = int(input())
    plan = [tuple(int(s) for s in input().split()) for _ in range(N)]
    yes = traveling(N, plan)
    print('Yes' if yes else 'No')
