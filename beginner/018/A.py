def mamemaki(A: int, B: int, C: int) -> list:
    if A < B and B < C:
        return [3, 2, 1]
    if A < C and C < B:
        return [3, 1, 2]
    if B < A and A < C:
        return [2, 3, 1]
    if B < C and C < A:
        return [1, 3, 2]
    if C < A and A < B:
        return [2, 1, 3]
    if C < B and B < A:
        return [1, 2, 3]
    return []


if __name__ == "__main__":
    A, B, C = [int(input()) for _ in range(3)]
    ans = mamemaki(A, B, C)
    for a in ans:
        print(a)
