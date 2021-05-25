#!/usr/bin/env python3
import sys


N, K = map(int, input().split())
S = input()

L = [[10**9 for _ in range(26)] for _ in range(len(S)+1)]
for s in range(len(S)-1, -1, -1):
    for i in range(26):
        if ord(S[s]) - ord('a') == i:
            L[s][i] = s
        else:
            L[s][i] = L[s+1][i]

t = ""
p = 0
for k in range(1, K+1):
    for i in range(26):
        np = L[p][i]
        pl = N - np - 1
        if pl >= K-k:
            t += chr(i+ord('a'))
            p = np + 1
            break

print(t)
