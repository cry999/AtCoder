def sentou(N: int, T: int, times: list) -> int:
    start_time, limit_time = 0, 0
    total_time = 0
    for t in times:
        if t >= limit_time:
            total_time += (limit_time - start_time)
            start_time = t
        limit_time = t + T
    return total_time + (limit_time - start_time)


if __name__ == "__main__":
    N, T = map(int, input().split())
    times = [int(s) for s in input().split()]
    ans = sentou(N, T, times)
    print(ans)
