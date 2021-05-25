#!/usr/bin/env python3
import sys
import math


def solve(T: int, case: "List[int]"):

    for c in case:

        m = c % 4

        if m == 0:
            print('Even')
        elif m == 2:
            print('Same')
        else:
            print('Odd')
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    case = [int(next(tokens)) for _ in range(T)]  # type: "List[int]"
    solve(T, case)


if __name__ == '__main__':
    main()
