#!/usr/bin/env python3
import sys


def solve(N: int, ST):
    st = sorted(ST, key=lambda x: int(x[1]))
    print(st[-2][0])
    return


# Generated by 2.2.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    ST = [list(map(str, input().split())) for l in range(N)]
    solve(N, ST)


if __name__ == '__main__':
    main()
