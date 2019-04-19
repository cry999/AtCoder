def temeperance(N: int, H: int, A: int, B: int, C: int, D: int, E: int)->int:
    min_price = float('inf')
    for x in range(N):
        # x*B + y*D + H - (N-x-y)*E > 0
        # y*(D+E) > N*E - H - (B+E)*x
        # y > {N*E - H - (B+E)*x} / (D+E)
        y = (N*E - H - (B+E)*x) // (D+E)
        if x*B + y*D + H - (N-x-y)*E <= 0:
            y += 1

        min_price = min(min_price, A*x + C*y)

    return min_price


if __name__ == "__main__":
    N, H = map(int, input().split())
    A, B, C, D, E = map(int, input().split())
    ans = temeperance(N, H, A, B, C, D, E)
    print(ans)
