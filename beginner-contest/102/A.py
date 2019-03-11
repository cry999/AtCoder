def multiple_of_2_and_N(N: int) -> int:
    return N if N % 2 == 0 else 2*N


if __name__ == "__main__":
    N = int(input())
    ans = multiple_of_2_and_N(N)
    print(ans)
