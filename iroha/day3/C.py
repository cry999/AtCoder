def not_say_no(N: int, K: int)->tuple:
    V, R = [0] * K, [0] * K
    children = [10 ** 14] * N

    for n in range(K-N):
        i = n % N
        V[n] = n+1
        R[n] = i+1
        children[i] -= n+1

    for i in range(N):
        V[i+K-N] = children[i]
        R[i+K-N] = i+1

    return V, R


if __name__ == "__main__":
    N, K = map(int, input().split())

    ansV, ansR = not_say_no(N, K)
    print(' '.join(map(str, ansV)))
    print('YES')
    print(' '.join(map(str, ansR)))
