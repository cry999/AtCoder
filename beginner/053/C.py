def x_yet_another_die_game(x: int)->int:
    n = x // 11
    if x == n * 11:
        return 2 * n
    if x <= n * 11 + 6:
        return 2 * n + 1
    return 2 * n + 2


if __name__ == "__main__":
    x = int(input())
    ans = x_yet_another_die_game(x)
    print(ans)
