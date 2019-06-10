def airplane(P: int, Q: int, R: int)->int:
    return min(P+Q, Q+R, R+P)


if __name__ == "__main__":
    P, Q, R = map(int, input().split())

    ans = airplane(P, Q, R)
    print(ans)
