def special_trains(N: int, CSF: list) -> list:
    res = []
    for i in range(N):
        t = 0
        for c, s, f in CSF[i:]:
            if t < s:
                t = s
            if t % f != 0:
                t = (t + f) - (t % f)
            t = t + c
        res.append(t)
    return res


if __name__ == "__main__":
    N = int(input())
    CSF = [tuple(map(int, input().split())) for _ in range(N-1)]
    ans = special_trains(N, CSF)
    for a in ans:
        print(a)
