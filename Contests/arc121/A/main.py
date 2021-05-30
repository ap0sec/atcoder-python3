#!/usr/bin/env python3
import sys
from operator import itemgetter
import itertools


def calc(x, i):

    L = list(itertools.combinations(x, 2))

    V = []
    for l in L:
        v = abs(l[0][i] - l[1][i])
        V.append([v, {l[0][2], l[1][2]}])

    return V


def solve(N: int, XY: "List[int]"):

    xy = [XY[n] + [n] for n in range(N)]

    xs = sorted(xy, key=itemgetter(0))
    ys = sorted(xy, key=itemgetter(1))

    xt = xs[:2] + xs[-2:]
    xt = [list(x) for x in set(tuple(x) for x in xt)]
    yt = ys[:2] + ys[-2:]
    yt = [list(x) for x in set(tuple(x) for x in yt)]

    xr = calc(xt, 0)
    yr = calc(yt, 1)

    U = []
    Up = []
    for r in sorted(xr + yr, reverse=True):
        if not r[1] in Up:
            U.append(r)
            Up.append(r[1])

    print(U[1][0])

    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():

    input = sys.stdin.readline

    N = int(input())  # type: int
    XY = [list(map(int, input().split())) for _ in range(N)]
    solve(N, XY)


if __name__ == '__main__':
    main()
