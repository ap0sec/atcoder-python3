#!/usr/bin/env python3
import sys
import re


MOD = 1000000007  # type: int

N = input()
S = input()

ctoi = {
    'a': 0,
    't': 1,
    'c': 2,
    'o': 3,
    'd': 4,
    'e': 5,
    'r': 6
}

s = ''.join(re.findall('a|t|c|o|d|e|r|', S))

dp = [[0 for _ in range(8)] for _ in range(len(s)+1)]

dp[0][0] = 1

for i in range(len(s)):
    for j in range(8):
        dp[i+1][j] += dp[i][j]
        if ctoi.get(s[i], -1) == j:
            dp[i+1][j+1] += dp[i][j]
    for j in range(8):
        dp[i+1][j] %= MOD
print(dp[len(s)][7])
