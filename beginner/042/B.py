def iroha_loves_strings(N: int, L: int, S: list) -> str:
    return ''.join(sorted(S))


if __name__ == "__main__":
    N = 0
    N, L = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = iroha_loves_strings(N, L, S)
    print(ans)
