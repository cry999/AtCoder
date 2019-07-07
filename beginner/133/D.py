def rain_flows_into_dams(N: int, A: list)->list:
    x = [0] * N
    x[0] = (sum(A[0::2])-sum(A[1::2])) // 2

    for i in range(1, N):
        x[i] = A[i-1] - x[i-1]

    return [2*y for y in x]


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]

    ans = rain_flows_into_dams(N, A)
    print(' '.join(map(str, ans)))
