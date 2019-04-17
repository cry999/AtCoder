from math import sqrt


def exponential(X: int) -> int:
    sq = int(sqrt(X) + 1)
    max_exp = 1
    for base in range(2, sq):
        num = 1
        while num * base <= X:
            num *= base
        max_exp = max(max_exp, num)
    return max_exp


if __name__ == "__main__":
    X = int(input())
    ans = exponential(X)
    print(ans)
