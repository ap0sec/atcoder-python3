#!/usr/bin/env python3
import sys


def main():

    input = sys.stdin.readline

    for i in range(1000):
        si, sj, ti, tj = map(int, input().split())

        print(si, sj, ti, tj)


if __name__ == '__main__':
    main()
