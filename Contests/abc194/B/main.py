#!/usr/bin/env python3
import sys


def solve(N, AB):

    minA = [10**6, None]
    minB = [None, 10**6]
    minAB = 10**11

    for ab in AB:
        if ab[0] < minA[0]:
            minA = ab
        if ab[1] < minB[1]:
            minB = ab
        if sum(ab) < minAB:
            minAB = sum(ab)

    print(minA, minB, minAB)


def main():

    input = sys.stdin.readline

    N = int(input())

    AB = [list(map(int, input().split())) for _ in range(N)]

    solve(N, AB)


if __name__ == '__main__':
    main()
