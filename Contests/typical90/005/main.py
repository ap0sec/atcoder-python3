#!/usr/bin/env python3
import numpy as np

N, B, K = map(int, input().split())
c = list(map(int, input().split()))

MOD = 10**9+7  # type: int
A = [[0 for _ in range(B)] for _ in range(B)]

for i in range(B):
    for j in range(K):
        nex = (10*i+c[j]) % B
        A[i][nex] += 1

A = np.array(A)
print(A)
# dp = [[0 for _ in range(B)] for _ in range(N+1)]


# dp[0][0] = 1

# print(dp[N][0])
