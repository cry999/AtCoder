def remainder_minimization_2019(L: int, R: int)->int:
    if R-L < 2018:
        ans = float('inf')
        for i in range(L, R):
            for j in range(i+1, R+1):
                ans = min(ans, (i * j) % 2019)

        return ans

    return 0


if __name__ == "__main__":
    L, R = map(int, input().split())

    ans = remainder_minimization_2019(L, R)
    print(ans)
