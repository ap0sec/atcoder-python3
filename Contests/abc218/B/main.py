#!/usr/bin/env python3
import sys


def solve(P: "List[int]"):

    b = ord('a')-1

    s = ''
    for p in P:
        s += chr(b+p)

    print(s)
        
    return


# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    P = [int(next(tokens)) for _ in range(26)]  # type: "List[int]"
    solve(P)

if __name__ == '__main__':
    main()