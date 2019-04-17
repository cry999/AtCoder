def restaurant(N: int) -> int:
    x = 800 * N
    y = 200 * (N // 15)
    return x - y


if __name__ == "__main__":
    N = int(input())
    ans = restaurant(N)
    print(ans)
