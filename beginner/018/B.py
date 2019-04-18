def reverse_string(S: str, N: int, queries: list) -> str:
    res = list(S)

    for l, r in queries:
        res = res[:l-1] + list(reversed(res[l-1:r])) + res[r:]

    return ''.join(res)


if __name__ == "__main__":
    S = input()
    N = int(input())
    queries = [tuple(int(s) for s in input().split()) for _ in range(N)]
    ans = reverse_string(S, N, queries)
    print(ans)
