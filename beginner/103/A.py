def task_scheduling_problem(A1: int, A2: int, A3: int)->int:
    return max(A1, A2, A3) - min(A1, A2, A3)


if __name__ == "__main__":
    A1, A2, A3 = map(int, input().split())
    ans = task_scheduling_problem(A1, A2, A3)
    print(ans)
