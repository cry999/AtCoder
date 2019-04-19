def flower_tells_fortune(n: int, A: list)->int:
    count = 0
    for a in A:
        if a % 6 == 1 or a % 6 == 3:
            # むしる必要はない
            continue
        if a % 6 == 2:
            count += 1
        elif a % 6 == 0:
            count += 3
        else:
            count += a % 6 - 3

    return count


if __name__ == "__main__":
    n = int(input())
    A = [int(s) for s in input().split()]
    ans = flower_tells_fortune(n, A)
    print(ans)
