def next_step(n: int):
    # 一の位のステップを決定
    d1 = n % 10
    if d1 < 3:  # 0, 1, 2
        step = 3 - d1
    elif d1 == 3:
        step = 2
    elif d1 < 5:  # 4
        step = 5 - d1
    elif d1 == 5:
        step = 2
    elif d1 < 7:  # 6
        step = 7 - d1
    else:  # 7, 8, 9
        step = 13 - d1

    # 10のくらい以上のステップを決定
    loop = 1
    nn = (n + step) // 10
    while nn > 0:
        d = nn % 10
        if d < 3:
            step += (3 - d) * (10 ** loop)
            nn += (3 - d)
        elif 3 < d and d < 5:
            step += (5 - d) * (10 ** loop)
            nn += (5 - d)
        elif 5 < d and d < 7:
            step += (7 - d) * (10 ** loop)
            nn += (7 - d)
        elif 7 < d:
            step += (13 - d) * (10 ** loop)
            nn += (13 - d)
        loop += 1
        nn //= 10

    return step


def q755(N: int) -> int:
    count = 0
    n = 357
    while n <= N:
        s = str(n)
        if not ('0' in s or '1' in s or '2' in s or '4' in s or '6' in s or '8' in s or '9' in s):
            if '3' in s and '5' in s and '7' in s:
                count += 1
        n += next_step(n)

    return count


if __name__ == "__main__":
    N = int(input())
    ans = q755(N)
    print(ans)
