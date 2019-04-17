def bugged(N: int, S: list)->int:
    not_ten = []
    not_ten_sum, ten_sum = 0, 0
    for s in S:
        if s % 10 == 0:
            ten_sum += s
        else:
            not_ten.append(s)
            not_ten_sum += s

    not_ten.sort()

    for s in not_ten:
        if not_ten_sum % 10 > 0:
            break
        not_ten_sum -= s

    return 0 if not_ten_sum == 0 else not_ten_sum + ten_sum


if __name__ == "__main__":
    N = int(input())
    S = [int(input()) for _ in range(N)]
    ans = bugged(N, S)
    print(ans)
