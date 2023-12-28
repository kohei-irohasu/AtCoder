# A問題
n = input()
print(n * int(n))


# B問題
# 辺の長さの種類は２種類のみ。
# 短い = 隣接している。
s = input()
t = input()
chr = 'ABCDEAEDCBA'
if (s in chr and t in chr) or (not s in chr and not t in chr):
    print('Yes')
else:
    print('No')
    

# C問題
# 答えとしてあり得る値を全探索。
# 各桁は1 ~ 3、単調増加、1の位は3。
# d: 何桁のレピュニットか。
# 小さい順に数える、単調増加だから、
# d,a,b,cの順でループ。
n = int(input())
for d in range(1, 13):
    for a in range(d - 1, -1, -1):
        for b in range(d - a - 1, -1, -1):
            c = d - a - b
            n -= 1
            if n == 0:
                result = '1' * a + '2' * b + '3' * c
                print(result)
                
# 別解
# sampleから最大でも12桁。
# 重複ありの場合のループ文の回し方。
n = int(input())
l = 12
r = [int('1' * (i + 1)) for i in range(l)]
for i in range(l):
    for j in range(i + 1):
        for k in range(j + 1):
            n -= 1
            if n == 0:
                print(r[i] + r[j] + r[k])


# D問題
# 頂点1の各子供の部分木の頂点数を求め、
# その最大の部分木を抜いた部分の合計を求めればよい。
# DFSで子供の頂点数を求める。
n = int(input())
g = [list() for _ in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

childs = g[1].copy()
m = len(childs)
cnt = [0] * m
for i in range(m):
    stack = []
    stack.append([childs[i], 1])  #[頂点, 親]
    while stack:
        u, p = stack.pop()
        cnt[i] += 1
        for v in g[u]:
            if v == p:  # 葉だったら、とばす。
                continue
            stack.append([v, u])

cnt = sorted(cnt)    
print(sum(cnt[:-1]) + 1)