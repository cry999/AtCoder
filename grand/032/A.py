def limited_insertion(N: int, B: list) -> list:
    op = []
    for i in range(N-1, -1, -1):
        for j in range(i, -1, -1):
            b = B[j]
            if i+1 < b:
                # invalid number
                return []
            if j+1 == b:
                # remove b[j]
                B = B[:j] + B[j+1:]
                op.append(b)
                break
        else:
            # not found
            return []
    return reversed(op)


if __name__ == "__main__":
    N = int(input())
    B = [int(s) for s in input().split()]

    ans = limited_insertion(N, B)
    if ans:
        for a in ans:
            print(a)
    else:
        print(-1)
