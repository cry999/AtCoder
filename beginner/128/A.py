def apple_pie(A: int, P: int)->int:
    return (A*3 + P)//2


if __name__ == "__main__":
    A, P = map(int, input().split())

    ans = apple_pie(A, P)
    print(ans)
