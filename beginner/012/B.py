def bathtime(N: int)->str:
    SECOND = 1
    MINUTE = 60*SECOND
    HOUR = 60*MINUTE

    h = N//HOUR
    N -= h * HOUR

    m = N//MINUTE
    N -= m * MINUTE

    s = N//SECOND
    N -= s * SECOND

    return '{:02}:{:02}:{:02}'.format(h, m, s)


if __name__ == "__main__":
    N = int(input())
    ans = bathtime(N)
    print(ans)
