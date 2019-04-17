def boxes_and_candies(N: int, x: int, A: list) -> int:
    count = 0
    for i in range(1, N):
        a1, a2 = A[i - 1], A[i]
        # print(a1, a2)

        if a1 + a2 <= x:
            # OK
            # print('--> OK')
            continue

        diff = (a1 + a2) - x
        count += diff
        # print('--> {}'.format(diff))

        if a2 > diff:
            A[i] -= diff
        else:
            A[i-1] -= diff - A[i]
            A[i] = 0

    return count


if __name__ == "__main__":
    N, x = map(int, input().split())
    A = [int(s) for s in input().split()]
    ans = boxes_and_candies(N, x, A)
    print(ans)
