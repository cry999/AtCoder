N = 0
N, A, B, C = [int(s) for s in input().split()]

bamboos = [int(input()) for _ in range(N)]


# def divide(l):
#     if len(l) == 0:
#         return []
#     if len(l) == 1:
#         return [
#             [[], [], []],  # 使わない
#             [[l[0]], [], []],  # A で使う
#             [[], [l[0]], []],  # B で使う
#             [[], [], [l[0]]],  # C で使う
#         ]

#     res = []
#     for a, b, c in divide(l[1:]):
#         # 使わない
#         res.append([a, b, c])
#         # A で使う
#         res.append([l[0:1] + a, b, c])
#         # B で使う
#         res.append([a, l[0:1] + b, c])
#         # C で使う
#         res.append([a, b, l[0:1] + c])

#     return res


# min_mp = -1
# for a, b, c in divide(bamboos):
#     al, ac = sum(a), len(a)
#     bl, bc = sum(b), len(b)
#     cl, cc = sum(c), len(c)
#     if al == 0 or bl == 0 or cl == 0:
#         continue

#     # 合成に使った魔力
#     composite = 10 * ((ac - 1) + (bc - 1) + (cc - 1))
#     # 総合魔力
#     mp = abs(al - A) + abs(bl - B) + abs(cl - C) + composite

#     if mp < min_mp or min_mp == -1:
#         min_mp = mp

# print(min_mp)

# ------------------------
# dfs を使うともっと短くかける
# ------------------------
def dfs(l, a, b, c):
    global A, B, C
    INF = 10**18
    if len(l) == 0:
        if min(a, b, c) > 0:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        else:
            return INF

    ret0 = dfs(l[1:], a, b, c)  # l[0] を使わない
    retA = dfs(l[1:], a + l[0], b, c) + 10  # l[0] を A で使う
    retB = dfs(l[1:], a, b + l[0], c) + 10  # l[0] を B で使う
    retC = dfs(l[1:], a, b, c + l[0]) + 10  # l[0] を C で使う

    return min(ret0, retA, retB, retC)


print(dfs(bamboos, 0, 0, 0))
