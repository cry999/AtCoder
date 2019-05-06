def rolling_the_old_man_and_the_sea(S: str, K: int)->str:
    K %= len(S)
    return S[K:] + S[:K]


if __name__ == "__main__":
    S = input()
    K = int(input())

    ans = rolling_the_old_man_and_the_sea(S, K)
    print(ans)
