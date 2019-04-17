def decrease(K: int)->list:
    ret = [i + (K//50) for i in range(50)]
    for i in range(K % 50):
        for j in range(50):
            if j == i:
                ret[j] += 50
            else:
                ret[j] -= 1

    return ret


if __name__ == "__main__":
    K = int(input())
    ans = decrease(K)
    print(len(ans))
    print(' '.join(map(str, ans)))
