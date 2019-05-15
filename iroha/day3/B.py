import sys


def iroha_chan()->int:
    print('? 0 1 2', flush=True)
    firstq = input()

    S, R, T = [0, 0], [0, 0], [0, 0]
    Tset = [set(), set()]
    for i in range(3, 8):
        for j in range(i+1, 8):
            for k in range(j+1, 8):
                print('? {} {} {}'.format(i, j, k), flush=True)
                q = input().split()

                for n in range(2):
                    if q[n][0] == 'S':
                        S[n] += 1
                    elif q[n][0] == 'R':
                        R[n] += 1
                    else:
                        Tset[n].add(i)
                        Tset[n].add(j)
                        Tset[n].add(k)
                        T[n] += 1

    ans = ''
    if firstq[0] == 'S':
        ans = '1' if S[0] == 6 else '2'
    elif firstq[0] == 'R':
        ans = '1' if R[0] == 6 else '2'
    else:  # firstq[0] == 'T'
        ans = '1' if T[1] != 4 or len(Tset[0]) == 4 else '2'

    print('!' + ans, flush=True)


if __name__ == "__main__":
    iroha_chan()
