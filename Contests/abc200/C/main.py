#!/usr/bin/env python3
import sys
import math

N = input()
A = [i % 200 for i in list(map(int, input().split()))]

print(f"A = {A}")

count = 0
for i in range(200):
    c = A.count(i)
    if not c < 2:
        count += math.factorial(c) / (2 * math.factorial((c - 2)))

print(int(count))
