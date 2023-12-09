# A問題
n, x = map(int, input().split())
s = list(map(int, input().split()))

ans = 0
for i in s:
    if i <= x:
        ans += i
print(ans)


# B問題
# 素直にset()使う。
n = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    for j in range(1, d[i - 1] + 1):
        if len(set(str(i) + str(j))) == 1:
            ans += 1
print(ans)


# C問題
# 全探索はTLE。l文字目からr文字目みたいな
# 差を考える問題は累積和の定番。
n, q = map(int, input().split())
s = input()
lr = [map(int, input().split()) for _ in range(q)]

b = [0]
for i in range(n - 1):
    if s[i] == s[i + 1]:
        b.append(b[- 1] + 1)
    else:
        b.append(b[- 1])

for l, r in lr:
    print(b[r - 1] - b[l - 1])