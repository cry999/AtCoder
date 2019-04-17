def chocolate(N: int, D: int, X: int, A: list) -> int:
    # i 人目の参加者が食べる個数を m とすると、m は
    # (m-1)ai + 1 <= D
    # を満たす最大の m である。したがって、これを変形して、
    # m = 1 + (D-1)//ai
    # となる。
    # これを各 i について和をとって、残った X 個を足せば
    # 初日に用意されていた個数が算出できる。
    return X + sum(1 + (D-1)//a for a in A)


if __name__ == "__main__":
    N = int(input())
    D, X = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    ans = chocolate(N, D, X, A)
    print(ans)
