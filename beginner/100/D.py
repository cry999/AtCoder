def patisserie_ABC(N: int, M: int, XYZ: list) -> int:
    ans = 0
    for n in range(8):
        d1 = 1 if n % 2 > 0 else -1
        d2 = 1 if (n // 2) % 2 > 0 else -1
        d3 = 1 if (n // 4) % 2 > 0 else -1

        sorted_XYZ = sorted([
            d1*x + d2*y + d3*z for x, y, z in XYZ],
            reverse=True)
        ans = max(ans, abs(sum(sorted_XYZ[:M])))

    return ans


if __name__ == "__main__":
    N, M = map(int, input().split())
    XYZ = [tuple(int(s) for s in input().split()) for _ in range(N)]
    ans = patisserie_ABC(N, M, XYZ)
    print(ans)
