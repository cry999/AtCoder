import bisect
import collections


def sequence_decomposing(N: int, A: list)->int:
    mins = collections.deque([A[0]])

    for a in A[1:]:
        i = bisect.bisect_left(mins, a)
        if i == 0:
            mins.appendleft(a)
        else:
            mins[i-1] = a

    return len(mins)


if __name__ == "__main__":
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = sequence_decomposing(N, A)
    print(ans)
