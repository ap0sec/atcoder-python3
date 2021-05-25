#!/usr/bin/env python3
import sys


def solve(t: int, N: int):

    before = 0
    rule = []
    for i in range(1, 100+t):
        intax = ((100+t) * i)//100
        if intax - before > 1:
            rule.append(intax-1)

        before = intax

    q, r = divmod(N-1, t)
    print((100+t)*q + rule[r])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    t = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(t, N)


if __name__ == '__main__':
    main()
