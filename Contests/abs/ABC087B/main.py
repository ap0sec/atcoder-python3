#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int):
    count = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                if 500*a + 100*b + 50*c == X:
                    count += 1

    print(count)
    return


# Generated by 2.2.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(A, B, C, X)


if __name__ == '__main__':
    main()
