import numpy as np

H, W = map(int, input().split())
A = []
for _ in range(H):  # マスの情報を点数に置き換える　+→1、-→-1　Aに保存
    S = input()
    a = []
    for s in S:
        if s == '+':
            a.append(1)
        else:
            a.append(-1)
    A.append(a)

# dp[h][w] (h,w)からゴールした時の
# h+w→偶数:Takahashi、奇数：Aoki　得点差
INF = 10 ** 9
dp = [[-INF] * W for _ in range(H)]
for h in reversed(range(H)):  # hを降順に検索　今回reversed(range(H)を覚えた　添え字を間違えにくい
    for w in reversed(range(W)):  # wを降順に検索
        if h == H - 1 and w == W - 1:  # ゴールのマスにいるので引き分け
            dp[h][w] = 0
        else:  # 一つ先のマスで得られる得点から相手方から見た得点差を引くと、今のマスの自分から見た得点差になる
            if h + 1 < H:
                dp[h][w] = max(dp[h][w], A[h + 1][w] - dp[h + 1][w])
            if w + 1 < W:
                dp[h][w] = max(dp[h][w], A[h][w + 1] - dp[h][w + 1])
        print(np.array(dp))

if dp[0][0] > 0:
    ans = "Takahashi"
elif dp[0][0] < 0:
    ans = "Aoki"
else:
    ans = "Draw"
print(ans)
