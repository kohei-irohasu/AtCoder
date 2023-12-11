# A問題
s = input()
for i in s:
    print(i, end=" ")
    

# B問題
n = int(input())
a = list(map(int, input().split()))
m = max(a)
b = [i for i in a if i != m]
ans = max(b)
print(ans)

# 別解
n = int(input())
a = set(list(map(int, input().split())))

a = list(a)
a.sort(reverse=True)
print(a[1])


# C問題
# ランレングス圧縮というらしい？
# 各アルファベットの最大連続長を計算すればよい。
# aaaがあるなら、a,aa,aaaが存在し、数は3となるから
n = int(input())
s = input()

mx = [0] * 26  #  アルファベットは26文字
l = 0  # 全体のインデックス

while l < n:
    r = l + 1
    while r < n and s[l] == s[r]:
        r += 1
    c = ord(s[l]) - ord('a')
    mx[c] = max(mx[c], r - l)
    l = r

ans = sum(mx)
print(ans)


# D問題
# i+1票目に当選者になりうるのは、
# i票目時点の当選者か、i+1票目をもらった候補者のみ
n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = [0] * (n + 1)   # 各候補者の得票数
ans = 0               # 現時点での当選者

for i in range(m):
    cnt[a[i]] += 1
    if cnt[ans] < cnt[a[i]]:
        ans = a[i]
    elif cnt[ans] == cnt[a[i]]:
        ans = min(ans, a[i])
    print(ans)