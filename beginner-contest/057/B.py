def checkpoints(N: int, M: int, students: list, points: list)->list:
    ans = []
    for x, y in students:
        min_d, min_i = float('inf'), 0
        for i, (c, d) in enumerate(points):
            if abs(x-c) + abs(y-d) < min_d:
                min_d = abs(x-c) + abs(y-d)
                min_i = i
        ans.append(min_i)

    return ans


if __name__ == "__main__":
    N = 0
    M = 0
    N, M = map(int, input().split())
    students = [tuple(map(int, input().split())) for _ in range(N)]
    points = [tuple(map(int, input().split())) for _ in range(M)]
    ans = checkpoints(N, M, students, points)

    print('\n'.join(str(i+1) for i in ans))
