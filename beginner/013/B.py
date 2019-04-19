def lock(a: int, b: int)->int:
    return min(abs(a - b), abs(a+10-b), abs(a-10-b))


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    ans = lock(a, b)
    print(ans)
