def remaining_time(A: int, B: int)->int:
    return (A+B) % 24


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = remaining_time(A, B)
    print(ans)
