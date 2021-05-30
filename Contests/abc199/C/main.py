#!/usr/bin/env python3
import sys


def solve(N, S, Q, query):

    s = list(S)

    rfed = False

    for q in query:
        if q[0] == 1:
            a = q[1]-1
            b = q[2]-1
            if rfed:
                a = a+N if a < N else a-N
                b = b+N if b < N else b-N
            s[a], s[b] = s[b], s[a]
        else:
            rfed = not rfed

    if rfed:
        s = s[N:] + s[:N]
    print(''.join(s))


def main():
    input = sys.stdin.readline

    N = int(input())
    S = input()[:-1]
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    solve(N, S, Q, query)


if __name__ == '__main__':
    main()
