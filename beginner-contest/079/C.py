def train_ticket(A: int, B: int, C: int, D: int) -> str:
    # 演算子の組み合わせは高々 2^3 = 8 通りしかないので
    # 全探索で OK
    nums = [B, C, D]
    for i in range(1 << 3):
        s = A
        ans = str(A)
        for j in range(3):
            if i & 1 == 1:
                s += nums[j]
                ans += '+' + str(nums[j])
            else:
                s -= nums[j]
                ans += '-' + str(nums[j])
            i >>= 1

        if s == 7:
            return ans + '=7'
    return 'invalid test case'


if __name__ == "__main__":
    A, B, C, D = map(int, input())
    ans = train_ticket(A, B, C, D)
    print(ans)
