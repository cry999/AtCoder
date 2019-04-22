def shift_only(N: int, A: list) -> int:
    min_div = 31

    for ai in A:
        div = 0
        while ai > 0 and ai & 1 == 0 and min_div >= div:
            ai >>= 1
            div += 1
        min_div = min(div, min_div)

    return min_div


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]

    ans = shift_only(N, A)
    print(ans)
