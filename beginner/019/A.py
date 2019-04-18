def age(A: int, B: int, C: int)->int:
    return sorted([A, B, C])[1]


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    ans = age(A, B, C)
    print(ans)
