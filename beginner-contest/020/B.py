def addition(A: int, B: int)->int:
    return 2 * int(str(A) + str(B))


if __name__ == "__main__":
    A, B = map(int, input().split())

    ans = addition(A, B)
    print(ans)
