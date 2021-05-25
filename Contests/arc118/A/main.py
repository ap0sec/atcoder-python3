#!/usr/bin/env python3
import sys


def solve(t: int, N: int):

    before = 0
    before_target = -1

    rule = []
    for i in range(0, 150):
        intax = int((100+t)/100 * i)
        if intax - before > 1:
            print(intax-1, intax, before, (intax)-before_target)
            rule.append((intax)-before_target)
            before_target = intax-1

        before = intax

    print(rule)
    ret_val = (100+t)*(N // len(rule))
    for v in rule[:N % len(rule)]:
        ret_val += v

    print(ret_val-1)
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
