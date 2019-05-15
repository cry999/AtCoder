

def alien(
        A: int, B: int, C: int, D: int, E: int, F: int,
        G: int, H: int, I: int, J: int, K: int, L: int,
        M: int, N: int, O: int, P: int, Q: int, R: int,
        S: int, T: int, U: int, V: int, W: int, X: int,
        Y: int, Z: int)->list:
    dagabaji_dict = [
        '',
        'a',
        'aa',
        'aaa',
        'aaai',
        'aaaji',
        'aabaji',
        'agabaji',
        'dagabaji',
    ]
    perfect_numbers = [
        6,
        28,
        496,
        8128,
        3355033,
        8589869056,
        137438691328,
        2305843008139952128,
        2658455991569831744654692615953842176,
    ]
    f1 = K if K > 0 else 59
    m = 1
    while True:
        if f1 % 61 == L:
            if m == M:
                break
            else:
                m += 1
        f1 += 59

    f2 = perfect_numbers[-1]
    for p in perfect_numbers:
        if abs(f1-p) >= N:
            f2 = min(f2, p)

    return [
        A-B,
        C+D,
        F-E+1 if E <= F else 0,
        (G+H+I)//3 + 1,
        dagabaji_dict[J],
        min(f1, f2),
        max(f1, f2),
        ((O+P+Q) * (R+S+T) * (U+V+W) * (X+Y+Z)) % 9973,
    ]


if __name__ == "__main__":
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = map(
        int, input().split())

    for ans in alien(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z):
        print(ans)
