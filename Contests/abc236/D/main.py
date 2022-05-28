#!/usr/bin/env python3
from itertools import permutations


def solve(N: int, A: "List[list[int]]"):

    s = [i+1 for i in range(2*N)]
    l = []

    for it in permutations(s):
        st.add(it)
    print(sorted(st))


def main():
    N = int(input())
    A = [list(map(int, input().split())) for l in range(N+1)]

    solve(N, A)


if __name__ == '__main__':
    main()
