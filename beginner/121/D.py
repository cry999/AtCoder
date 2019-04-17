def compute_xor(n: int)->int:
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0


def xor_world(A: int, B: int)->int:
    return compute_xor(B) ^ compute_xor(A-1)


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = xor_world(A, B)
    print(ans)
