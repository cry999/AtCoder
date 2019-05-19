def changing_a_character(N: int, K: int, S: str)->str:
    return ''.join(c.lower() if i == K-1 else c for i, c in enumerate(S))


if __name__ == "__main__":
    N, K = map(int, input().split())
    S = input()

    ans = changing_a_character(N, K, S)
    print(ans)
