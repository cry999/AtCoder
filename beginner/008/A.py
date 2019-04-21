def album(S: int, T: int)->int:
    return T-S+1


if __name__ == "__main__":
    S, T = map(int, input().split())
    ans = album(S, T)
    print(ans)
