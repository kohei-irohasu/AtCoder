# A問題
M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d == D:
    d = 1
    if M == m:
        m = 1
        y += 1
    else:
        m += 1
else:
    d += 1

print(y, m, d)


# B問題
n, s, m, l = map(int, input().split())
ans = 10 ** 6

for i in range(18):
    for j in range(18):
        for k in range(18):
            if  6 * i + 8 * j + 12 * k >= n:
                ans = min(ans, i * s + j * m + k * l)
print(ans)


# C問題
# 全探索はTLE。降順に並んでいたら、o(n)でできる。
# sortしてもindex情報を保つため、dictで情報を管理して
# aの順番で出力していく。
# 同じ数字が存在するので累積和の様ではなく、tmpでこれまでの
# 数字を管理する。
n = int(input())
a = list(map(int, input().split()))

sort_a = sorted(a, reverse=True)
d = {sort_a[0] : 0}
tmp = 0
for i in range(n - 1):
    if sort_a[i + 1] != sort_a[i]:
        d[sort_a[i + 1]] = tmp + sort_a[i]
    tmp += sort_a[i]
    
print(*[d[i] for i in a])


# D問題
# 累積和。グリッドはnの周期で繰り返し。
# 2次元の累積和。
n, q = map(int, input().split())
p = list(input() for _ in range(n))

# 2次元配列の累積和の計算
pcsum = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        pcsum[i + 1][j + 1] = pcsum[i][j + 1] + pcsum[i + 1][j] - pcsum[i][j]
        if p[i][j] == 'B':
            pcsum[i + 1][j + 1] += 1

# i, jまでの部分和の計算
def f(i, j):
    ans = 0
    ans += (i // n) * (j // n) * pcsum[n][n]    # n*nグリッドが何個あるか？
    ans += (j // n) * pcsum[i % n][n]     # 下に横に何個あるか？     
    ans += (i // n) * pcsum[n][j % n]     # 横に縦に何個あるか？
    ans += pcsum[i % n][j % n]  # 最後のあまり1マス分
    
    return ans

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    x2, y2 = x2 + 1, y2 + 1
    print(f(x2, y2) + f(x1, y1) - f(x1, y2) - f(x2, y1))
