def christmas_eve_eve(N: int, P: list) -> int:
    p_max = max(P)
    return sum(P) - (p_max // 2)


if __name__ == "__main__":
    N = int(input())
    P = [int(input()) for _ in range(N)]
    ans = christmas_eve_eve(N, P)
    print(ans)
