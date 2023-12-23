# A問題
n, s, k = map(int, input().split())
ans = 0
for i in range(n):
    p, q = map(int, input().split())
    ans += p * q

print(ans if ans >= s else ans + k)


# B問題
k, g, m = map(int, input().split())

G, M = 0, 0
for _ in range(k):
    if G == g:
        G = 0
    elif M == 0:
        M = m
    else:
        if M >= g - G:
            M -= g - G
            G += g - G
        else:
            G += M
            M = 0            
    
print(G, M)


# C問題
# 愚直に0,1,2で場合分けするversion
n, m = map(int, input().split())
s = input()

muzi = m
muzi_q = m
logo = 0
logo_q = 0
ans = 0
for i in s:
    if i == '1':
        if muzi == 0 and logo == 0:
            ans += 1
            logo_q += 1
        else:
            if muzi == 0:
                logo -= 1
            else:
                muzi -= 1
    elif i == '2':
        if logo == 0:
            ans += 1
            logo_q += 1
        else:
            logo -= 1
    else:
        muzi = muzi_q
        logo = logo_q

print(ans)

# 洗濯をリセットと考え、それまでの予定を独立して考え
# その独立した予定の中の必要なシャツの最大値を求める。
n, m = map(int, input().split())
s = input().split('0')

ans = 0
for i in s:
    muzi = i.count('1')
    logo = i.count('2')
    if (muzi + logo) > (ans + m):
        ans += (muzi + logo) - (ans + m)
    if logo > ans:
        ans = logo
print(ans) 


# D問題
# 数が小さいので幅優先探索。
# 最小手数 = 最短経路 = BFS
from collections import deque

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

# 辞書のキーは不変なオブジェクトである必要があるから
start_state = tuple(map(tuple, a))
target_state = tuple(map(tuple, b))

d = {start_state: 0}
q = deque([a])

while q:
    a = q.popleft()
    
    for i in range(h - 1):
        b = [row[:] for row in a]
        b[i], b[i + 1] = b[i + 1], b[i]
        
        # すでにその行列をチェックしているかどうか
        if tuple(map(tuple, b)) not in d:
            d[tuple(map(tuple, b))] = d[tuple(map(tuple, a))] + 1
            q.append(b)
    
    for j in range(w - 1):
        b = [row[:] for row in a]
        for i in range(h):
            b[i][j], b[i][j + 1] = b[i][j + 1], b[i][j]
        
        if tuple(map(tuple, b)) not in d:
            d[tuple(map(tuple, b))] = d[tuple(map(tuple, a))] + 1
            q.append(b)

print(d[target_state] if target_state in d else -1)