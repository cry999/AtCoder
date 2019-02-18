def double_landscape(N: int, M: int, A: list, B: list) -> int:
    if not (is_unique(A) and is_unique(B)):
        return 0

    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    i_a, i_b = 0, 0

    count = 1
    NM = N*M
    for x in range(NM, 0, -1):
        availables = 0
        if i_a < N and i_b < M and x == A[i_a] and x == B[i_b]:
            availables = 1
            i_a += 1
            i_b += 1
        elif i_a < N and x == A[i_a]:
            availables = i_b
            i_a += 1
        elif i_b < M and x == B[i_b]:
            availables = i_a
            i_b += 1
        else:
            availables = i_a * i_b - (NM - x)

        if availables <= 0:
            return 0

        count *= availables
        count %= 10**9 + 7

    return count


def is_unique(l: list) -> bool:
    return len(l) == len(set(l))


if __name__ == "__main__":
    N, M = [int(s) for s in input().split()]
    A = [int(s) for s in input().split()]
    B = [int(s) for s in input().split()]

    print(double_landscape(N, M, A, B))
