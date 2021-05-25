#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, t: "List[int]", x: "List[int]", y: "List[int]"):
    now = [0, 0]
    time = 0
    for i in range(N):
        diff_time = t[i] - time
        diff_xy = abs(now[0]-x[i]) + abs(now[1]-y[i])
        if diff_time < diff_xy or diff_time % 2 != diff_xy % 2:
            print(NO)
            return
        time = t[i]
        now = [x[i], y[i]]

    print(YES)
    return


# Generated by 2.2.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    t = [int()] * (N)  # type: "List[int]"
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, t, x, y)


if __name__ == '__main__':
    main()