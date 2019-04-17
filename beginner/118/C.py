def __gcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return __gcd(b, a % b)


def monsters_battle_royale(N: int, A: list) -> int:
    a = A[0]
    for b in A[1:]:
        a = __gcd(a, b)

    return a


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = monsters_battle_royale(N, A)
    print(ans)
