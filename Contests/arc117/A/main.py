#!/usr/bin/env python3
import sys


def solve(A: int, B: int):

    if A >= B:
        AL = [i for i in range(1, A+1)]
        SA = int((A)/2*(A+1))
        BL = [i*(-1) for i in range(1, B)]
        SB = int((B-1)/2*(B))
        BL.append(SB-SA)

        print(' '.join(list(map(str, AL))+list(map(str, BL))))

    if A < B:
        AL = [i for i in range(1, A)]
        SA = int((A-1)/2*(A))
        BL = [i*(-1) for i in range(1, B+1)]
        SB = int((B)/2*(B+1))
        AL.append(SB-SA)

        print(' '.join(list(map(str, AL))+list(map(str, BL))))

    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)


if __name__ == '__main__':
    main()