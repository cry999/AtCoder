def dfs(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]

    # + を先頭の数字の後ろに入れる
    n1 = nums[0] * (1 << (len(nums) - 2)) + dfs(nums[1:])

    # + をいれない。
    headless = nums[1:]
    headless[0] += nums[0] * 10
    n2 = dfs(headless)

    return n1 + n2


def many_formulas(s: str) -> int:
    nums = list(map(int, s))
    return dfs(nums)


if __name__ == "__main__":
    s = input()
    ans = many_formulas(s)
    print(ans)
