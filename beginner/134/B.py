def golden_apple(N: int, D: int)->int:
    ans = N // (2*D+1)
    if N % (2*D+1):
        ans += 1
    return ans


if __name__ == "__main__":
    N, D = map(int, input().split())
    ans = golden_apple(N, D)
    print(ans)
