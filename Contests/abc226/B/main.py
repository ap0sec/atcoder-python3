#!/usr/bin/env python3

def solve(L: list):
    print(len(list(set(L))))
    return


def main():
    N = int(input())
    L = [input() for _ in range(N)]

    solve(L)


if __name__ == '__main__':
    main()
