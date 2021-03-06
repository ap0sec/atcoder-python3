#!/usr/bin/env python3
import sys


def bs(ok, ng, target):
    while ng - ok > 1:
        p = (ok + ng) // 2
        if check(p, target):
            ok = p
        else:
            ng = p

    return ok


def check(x, target) -> bool:
    L = target[0]
    K = target[1]
    A = target[2]

    p = 0
    count = 0
    for i in A:
        if i-p >= x and count < K:
            count += 1
            p = i

    if L-p < x or K-count != 0:
        return False

    return True


def solve(N: int, L: int, K: int, A: "List[int]"):
    print(bs(0, L, [L, K, A]))
    return


# Generated by 2.2.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L, K, A)


if __name__ == '__main__':
    main()
