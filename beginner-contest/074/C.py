def sugar_water(A: int, B: int, C: int, D: int, E: int, F: int)->tuple:
    max_dens = 0
    min_a, min_b, min_c, min_d = 0, 0, 0, 0
    for a in range(F//(100*A) + 1):
        for b in range((F-100*A*a)//(100*B) + 1):
            for c in range((F-100*A*a-100*B*b)//C + 1):
                for d in range((F-100*A*a-100*B*b-c*C)//D + 1):
                    if F < 100*A*a + 100*B*b + c + d:
                        continue
                    if E * (100*a*A + 100*b*B) < (c*C + d*D) * 100:
                        continue
                    if a == 0 and b == 0 and c == 0 and d == 0:
                        continue

                    dens = (c*C + d*D) / (100*a*A + 100*b*B + c*C + d*D)

                    if max_dens < dens:
                        min_a, min_b, min_c, min_d = a, b, c, d
                        max_dens = dens
    if min_a == 0 and min_b == 0 and min_c == 0 and min_d == 0:
        min_a = 1
    return 100*A*min_a + 100*B*min_b + C*min_c + D*min_d, C*min_c + D*min_d


if __name__ == "__main__":
    A, B, C, D, E, F = map(int, input().split())
    w, s = sugar_water(A, B, C, D, E, F)
    print(w, s)
