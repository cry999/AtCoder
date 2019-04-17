def time_limit_exceeded(N: int, T: int, CT: list) -> int:
    min_cost = float('inf')
    for c, t in CT:
        if t > T:
            continue
        if min_cost > c:
            min_cost = c
    return min_cost


if __name__ == "__main__":
    N, T = map(int, input().split())
    CT = [tuple(int(s) for s in input().split()) for _ in range(N)]
    ans = time_limit_exceeded(N, T, CT)
    print(ans if ans != float('inf') else 'TLE')
