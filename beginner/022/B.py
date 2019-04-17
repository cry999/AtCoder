def bumble_bee(N: int, A: list) -> int:
    count = 0
    exist = set()

    for a in A:
        if a in exist:
            count += 1
        else:
            exist.add(a)
    return count


if __name__ == "__main__":
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = bumble_bee(N, A)
    print(ans)
