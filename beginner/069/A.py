def k_city(n: int, m: int)->int:
    return (n-1)*(m-1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    ans = k_city(n, m)
    print(ans)
