def islands_war(N: int, M: int, AB: list)->int:
    latest_remvoed = 0
    removed_num = 0
    for a, b in sorted(AB, key=lambda x: x[1]):
        if a <= latest_remvoed:
            continue
        latest_remvoed = b - 1
        removed_num += 1
    return removed_num


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    ans = islands_war(N, M, AB)
    print(ans)
