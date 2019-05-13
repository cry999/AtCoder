def rgb_boxes(R: int, G: int, B: int, N: int)->int:
    res = 0
    for r in range(N+1):
        if r * R > N:
            break
        for g in range(N+1):
            if r * R + g * G > N:
                break
            if (N - (r*R + g*G)) % B == 0:
                res += 1

    return res


if __name__ == "__main__":
    R, G, B, N = map(int, input().split())

    ans = rgb_boxes(R, G, B, N)
    print(ans)
