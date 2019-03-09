def rated_for_me(R: int)->str:
    if R < 1200:
        return 'ABC'
    if R < 2800:
        return 'ARC'
    return 'AGC'


if __name__ == "__main__":
    R = int(input())
    ans = rated_for_me(R)
    print(ans)
