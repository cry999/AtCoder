def procon(scores: list) -> int:
    res = 0
    for s, e in scores:
        res += s * e
    return res // 10


if __name__ == "__main__":
    scores = [tuple(int(s) for s in input().split()) for _ in range(3)]
    ans = procon(scores)
    print(ans)
