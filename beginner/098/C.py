def attention(N: int, S: str) -> int:
    # 西から順に i 人までのうち西を向いている人の数
    Se = [0] * (N + 1)
    for i, c in enumerate(S):
        Se[i + 1] = Se[i] + (1 if c == 'W' else 0)

    min_people = float('inf')
    for i, c in enumerate(S):
        w2e = Se[i]  # 西から東に向きを変える人数
        e2w = (N - (i + 1)) - (Se[N] - Se[i + 1])
        min_people = min(min_people, w2e + e2w)

    return min_people


if __name__ == "__main__":
    N = int(input())
    S = input()
    ans = attention(N, S)
    print(ans)
