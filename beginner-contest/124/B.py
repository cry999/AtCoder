def great_ocean_view(N: int, H: list)->int:
    max_h = 0
    count = 0
    for h in H:
        if max_h <= h:
            count += 1
            max_h = h
    return count


if __name__ == "__main__":
    N = int(input())
    H = [int(s) for s in input().split()]
    ans = great_ocean_view(N, H)
    print(ans)
