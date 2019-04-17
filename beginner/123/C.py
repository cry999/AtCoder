from math import ceil


def five_transportations(N: int, A: int, B: int, C: int, D: int, E: int)->int:
    return 5 + ceil(N / min(A, B, C, D, E)) - 1


if __name__ == "__main__":
    inputs = [int(input()) for _ in range(6)]
    N, A, B, C, D, E = inputs
    ans = five_transportations(N, A, B, C, D, E)
    print(ans)
