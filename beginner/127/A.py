def ferris_wheel(A: int, B: int)->int:
    if A >= 13:
        return B
    elif A >= 6:
        return B//2
    else:
        return 0


if __name__ == "__main__":
    A, B = map(int, input().split())

    ans = ferris_wheel(A, B)
    print(ans)
