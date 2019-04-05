def scc_puzzle(N: int, M: int) -> int:
    if 2 * N < M:
        # c が余る場合、余った c が 4 つごとに
        # 1 組みの `Scc` が作れる。
        return N + (M - 2 * N) // 4

    return M // 2


if __name__ == "__main__":
    N, M = map(int, input().split())
    ans = scc_puzzle(N, M)
    print(ans)
