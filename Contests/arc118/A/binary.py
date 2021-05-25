#!/usr/bin/env python3
import sys

MAX_N = sys.maxsize


def bs(ok, ng, target):
    while ok < ng:
        p = (ok + ng) // 2
        res = check(p, target)
        if res:
            ok = p+1
        else:
            ng = p

    return ng


def check(x, target) -> bool:
    intax = target[0]
    N = target[1]

    if intax*x - x < N:
        return True
    else:
        return False


def solve(t: int, N: int):
    intax_val = (100+t)/100

    print(int(intax_val*bs(-1, MAX_N+1, [intax_val, N]))-1)

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
