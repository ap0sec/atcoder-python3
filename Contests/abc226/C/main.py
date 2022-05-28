#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2*(10**5)+1)

N = int(input())
L = [list(map(int, input().split())) for l in range(N)]

TA = [[l[0], l[2:]] for l in L]

kl = {N}


def get_dependency(targets: list):

    v = 0
    for t in targets:
        if t in kl:
            continue
        else:
            kl.add(t)
            v += TA[t-1][0]
            v += get_dependency(TA[t-1][1])

    return v


def main():
    print(TA[N-1][0] + get_dependency(TA[N-1][1]))


if __name__ == '__main__':
    main()
