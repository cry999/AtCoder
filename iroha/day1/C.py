def halcyon_days(N: int)->list:
    return [N-7+i for i in range(8)]


if __name__ == "__main__":
    N = int(input())

    ans = halcyon_days(N)
    for a in ans:
        print(a)
