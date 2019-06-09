def delicious_burgers(N: int, K: int, S: str)->int:
    level = [0] * (N+1)

    for i, c in enumerate(S):
        if c == '(':
            level[i+1] = level[i]+1
        else:
            level[i+1] = level[i]-1

    # print(level)
    level.sort(reverse=True)

    return sum(lev for lev in level[:K])


if __name__ == "__main__":
    N, K = map(int, input().split())
    S = input()

    ans = delicious_burgers(N, K, S)
    print(ans)
