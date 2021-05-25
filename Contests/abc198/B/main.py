#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: str):

    pad = ""

    for n in N[::-1]:
        if n == '0':
            pad += '0'
        else:
            break

    N = pad + N

    if N == N[::-1]:
        print(YES)
    else:
        print(NO)

    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = str(next(tokens))  # type: str
    solve(N)


if __name__ == '__main__':
    main()