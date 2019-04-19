#! /usr/bin/env python
import random
import sys


if __name__ == "__main__":
    argv = sys.argv

    if len(argv) != 3:
        print('USAGE: {} K M'.format(argv[0]))
        sys.exit(1)

    K, M = int(sys.argv[1]), int(sys.argv[2])
    A = [str(random.randint(0, 1 << 32)) for _ in range(K)]
    C = [str(random.randint(0, 1 << 32)) for _ in range(K)]

    print(K, M)
    print(' '.join(A))
    print(' '.join(C))
