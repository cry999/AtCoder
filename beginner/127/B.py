def algae(r: int, D: int, x2000: int)->int:
    x = x2000

    res = []
    for _ in range(10):
        x = r*x - D
        res.append(x)

    return res


if __name__ == "__main__":
    r, D, x2000 = map(int, input().split())

    for ans in algae(r, D, x2000):
        print(ans)
