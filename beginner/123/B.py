def five_dishes(A: int, B: int, C: int, D: int, E: int)->int:
    dishes = sorted([A, B, C, D, E], key=lambda x: x % 10 if x % 10 else 10)

    def offset(d: int)->int:
        return 10 - d % 10 if d % 10 else 0

    return dishes[0] + sum(d + offset(d) for d in dishes[1:])


if __name__ == "__main__":
    inputs = [int(input()) for _ in range(5)]
    A, B, C, D, E = inputs
    ans = five_dishes(A, B, C, D, E)
    print(ans)
