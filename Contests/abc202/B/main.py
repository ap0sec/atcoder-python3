#!/usr/bin/env python3
import sys


def solve(S: str):

    s = S[::-1]

    s = s.replace("6", "^")
    s = s.replace("9", "$")
    s = s.replace("^", "9")
    s = s.replace("$", "6")

    print(s)

    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()