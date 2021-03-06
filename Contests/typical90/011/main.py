#!/usr/bin/env python3
import sys

input = sys.stdin.readline
N = int(input())
J = [list(map(int, input().split())) for _ in range(N)]

J = sorted(J)

MAX_D = 5001

# dp[i][j]: i個目までの仕事について考慮した場合(j時間経過)の最大金額
# J[i][0]: 締め切り,
# J[i][1]: 工数,
# J[i][2]: 報酬

dp = [[0 for _ in range(MAX_D)] for _ in range(N+1)]


def solve():
    for i in range(N):
        for j in range(MAX_D):
            nex = j + J[i][1]
            if nex <= J[i][0] and nex <= 5000:
                dp[i + 1][nex] = max(dp[i + 1][nex], dp[i][j] + J[i][2])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

    print(max(dp[N]))
    return


# Generated by 2.2.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    solve()


if __name__ == '__main__':
    main()
