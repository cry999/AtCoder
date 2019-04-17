def derangement(N: int, P: list)->int:
    count = 0
    for i in range(N-1):
        if P[i] == i+1:
            count += 1
            P[i], P[i+1] = P[i+1], P[i]

    if P[-1] == N:
        count += 1
    return count


if __name__ == "__main__":
    N = int(input())
    P = [int(s) for s in input().split()]
    ans = derangement(N, P)
    print(ans)
