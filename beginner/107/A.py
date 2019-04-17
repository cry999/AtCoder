def train(N: int, i: int)->int:
    return N - i + 1


if __name__ == "__main__":
    N, i = map(int, input().split())
    ans = train(N, i)
    print(ans)
