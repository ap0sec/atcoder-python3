#!/usr/bin/env python3
import sys


def solve(N: int, CP, Q: int, LR):

    prev = [[0, 0] for _ in range(N+1)]

    for i, cp in enumerate(CP):
        if cp[0] == 1:
            prev[i+1][0] += prev[i][0] + cp[1]
            prev[i+1][1] += prev[i][1]
        else:
            prev[i+1][0] += prev[i][0]
            prev[i+1][1] += prev[i][1] + cp[1]

    for q in LR:
        c1 = prev[q[1]][0] - prev[q[0]-1][0]
        c2 = prev[q[1]][1] - prev[q[0]-1][1]
        print(' '.join(map(str, [c1, c2])))

    return


def main():

    input = sys.stdin.readline

    N = int(input())  # type: int
    CP = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())  # type: int
    LR = [list(map(int, input().split())) for _ in range(Q)]
    solve(N, CP, Q, LR)


if __name__ == '__main__':
    main()
