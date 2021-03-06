#!/usr/bin/env python3
import sys


def bs(ok, ng, target):
    while ng - ok > 1:
        p = (ok + ng) // 2
        # print(p)
        res = check(p, target)
        # print(res)
        if res:
            ok = p
        else:
            ng = p

    return ok


def check(x, target) -> bool:
    bA = [sum([-1 if i < x else 1 for i in j]) for j in target]
    if min(bA) <= 0:
        return False
    else:
        return True


def solve(N: int, K: int, A: "List[List[int]]"):

    t = []

    for i in range(N-K+1):
        for j in range(N-K+1):
            v = []
            for k in range(K):
                v += A[j+k][i:i+K]

            t.append(v)
    print(bs(0, 10**9, t))
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, K, A)


if __name__ == '__main__':
    main()
