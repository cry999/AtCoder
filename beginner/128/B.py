def guidebook(N: int, scores: list)->list:
    rev = {v: i for i, v in enumerate(scores)}
    scores.sort(key=lambda x: -x[1])
    scores.sort(key=lambda x: x[0])

    return [rev[v]+1 for v in scores]


if __name__ == "__main__":
    N = int(input())
    scores = []
    for _ in range(N):
        s, p = input().split()
        scores.append((s, int(p)))

    for ans in guidebook(N, scores):
        print(ans)
