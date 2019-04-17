def pair(K: int)->int:
    even = K // 2
    odd = K // 2 + (0 if K % 2 == 0 else 1)

    return even * odd


if __name__ == "__main__":
    K = int(input())
    ans = pair(K)
    print(ans)
