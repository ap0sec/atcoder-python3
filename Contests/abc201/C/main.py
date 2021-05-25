#!/usr/bin/env python3
import sys


def solve(S: str):

    count = 0
    for i in range(10000):
        t = str(i).zfill(4)
        f = True
        for j in range(10):
            if S[j] == 'o' and not str(j) in t:
                f = False
                break
            if S[j] == 'x' and str(j) in t:
                f = False
                break

        if f:
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
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()