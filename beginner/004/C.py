def swap(N: int)->str:
    res = list('123456')
    for n in range(N % 30):
        res[n % 5], res[(n % 5)+1] = res[(n % 5)+1], res[n % 5]
    return ''.join(res)


if __name__ == "__main__":
    N = int(input())
    ans = swap(N)
    print(ans)
