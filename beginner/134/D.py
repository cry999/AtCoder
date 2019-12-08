def divisors(n: int)->list:
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i


def preparing_boxes(N: int, A: list)->list:
    B = []
    # C = [0] * N

    for i in range(N, 0, -1):
        # print('=== {} ==='.format(i))
        a = A[i-1]
        if a == 0:
            continue
        B.append(i)
        # C[i-1] = 1

        for div in divisors(i):
            # print(div)
            A[div-1] = 1 - A[div-1]

    # print(''.join(str(i) for i in C))

    return B


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    ans = preparing_boxes(N, A)
    print(len(ans))
    print(' '.join(str(i) for i in ans))
