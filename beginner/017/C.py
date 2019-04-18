def highscore(N: int, M: int, queries: list) -> int:
    s_left, s_right = [0] * (M+2), [0] * (M+2)

    for l, r, s in queries:
        s_left[r] += s
        s_right[l] += s

    for i in range(1, M):
        s_left[i] += s_left[i-1]
        s_right[M-i] += s_right[M-(i-1)]

    max_score = 0
    for i in range(1, M+1):
        max_score = max(max_score, s_left[i-1] + s_right[i+1])

    return max_score


if __name__ == "__main__":
    N = 0
    N, M = map(int, input().split())
    queries = [tuple(int(s) for s in input().split()) for _ in range(N)]
    ans = highscore(N, M, queries)
    print(ans)
