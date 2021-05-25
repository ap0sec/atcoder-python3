#!/usr/bin/env python3
from sys import stdin

H, W = map(int, stdin.readline().split())
A = []
for _ in range(H):
    A.append([1 if s == "+" else -1 for s in input()])

# A = [stdin.readline()[:-1] for l in range(H)]

INF = 10 ** 9
dp = [[-INF] * W for _ in range(H)]  # H行W列目まで進んだ場面における自分-相手の最大スコア


# def f(x, y):
#     return 1 if A[x][y] == '+' else -1


def main():
    for h in range(H-1, -1, -1):
        for w in range(W-1, -1, -1):
            if h == H - 1 and w == W - 1:
                dp[h][w] = 0
            else:
                if h + 1 < H:
                    dp[h][w] = max(dp[h][w], A[h+1][w] - dp[h + 1][w])
                if w + 1 < W:
                    dp[h][w] = max(dp[h][w], A[h][w+1] - dp[h][w + 1])

    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")


if __name__ == '__main__':
    main()
