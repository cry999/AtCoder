def ajihon(N: int, A: int) -> tuple:
    member_num = 3
    team_num = N//member_num

    # 最小チーム数、最大チーム数
    return (A//3 + (1 if A % 3 else 0)), min(A, team_num)


if __name__ == "__main__":
    N, A = map(int, input().split())

    ans_min, ans_max = ajihon(N, A)
    print(ans_min, ans_max)
