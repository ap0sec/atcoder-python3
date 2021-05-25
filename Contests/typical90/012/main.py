#!/usr/bin/env python3
import sys


YES = "Yes"  # type: str
NO = "No"  # type: str

input = sys.stdin.readline
H, W = map(int, input().split())
Q = int(input())
q = [list(map(int, input().split())) for _ in range(Q)]

F = [[0 for _ in range(W)] for _ in range(H)]

S = []


def around_check(x, y):
    t = {f"{x-1},{y}", f"{x+1},{y}", f"{x},{y-1}", f"{x},{y+1}"}
    f = []
    for i, s in enumerate(S):
        if not s.isdisjoint(t):
            s.add(f"{x},{y}")
            f.append(i)
    if not f:
        S.append({f"{x},{y}"})
    else:
        ss = set()
        for i in f[::-1]:
            ss = ss.union(S.pop(i))

        S.append(ss)

    return


def query(q):
    if q[0] == 1:
        x = q[1] - 1
        y = q[2] - 1
        F[x][y] = 1
        around_check(x, y)

    elif q[0] == 2:
        x1 = q[1] - 1
        y1 = q[2] - 1
        x2 = q[3] - 1
        y2 = q[4] - 1

        for s in S:
            if f"{x1},{y1}" in s and f"{x2},{y2}" in s:
                print(YES)
                return
        print(NO)


def solve():
    for i in q:
        query(i)


def main():
    solve()


if __name__ == '__main__':
    main()
