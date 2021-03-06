#!/usr/bin/env python3
import sys


def solve(N: int, D: int, H: int, d: "List[int]", h: "List[int]"):

    ret_val = 0

    for i in range(len(d)):
        a = ((H - h[i])/(D - d[i]))
        b = H - (a * D)
        if ret_val < b:
            ret_val = b

    print(ret_val)
    return


# Generated by 2.2.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    d = [int()] * (N)  # type: "List[int]"
    h = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        d[i] = int(next(tokens))
        h[i] = int(next(tokens))
    solve(N, D, H, d, h)


if __name__ == '__main__':
    main()
