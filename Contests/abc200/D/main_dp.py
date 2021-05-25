#!/usr/bin/env python3
import sys

MOD = 200  # type: int
YES = "Yes"  # type: str
NO = "No"  # type: str


N = int(input())
A = [i % 200 for i in list(map(int, input().split()))]

dp = [[0 for _ in range(200)] for _ in range(N+1)]

dp[0][0] = 1
for i in range(N):
    for j in range(200):
        if (j + A[i]) % 200:
            dp[i+1][j] = dp[i][j] + dp[i][j-A[i]]
        else:
            dp[i+1][j] = dp[i][j]

if max(dp[N]) < 2:
    print(NO)
else:
    print(YES)
