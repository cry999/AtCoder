def balloons(N: int, M: int, A: list)->int:
    num_ballon = 0
    num_color = 0

    A.sort(key=lambda x: -x)

    for a in A:
        num_ballon += a
        num_color += 1

        if M <= num_ballon:
            break
    return num_color


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = [int(s) for s in input().split()]

    ans = balloons(N, M, A)
    print(ans)
