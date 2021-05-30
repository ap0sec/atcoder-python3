#!/usr/bin/env python3
import sys


def solve(N: int):

    l = len(str(N))//2

    count = 0
    for i in range(1, 10**l):
        if int(str(i)+str(i)) <= N:
            count += 1
        else:
            break

    print(count)
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()