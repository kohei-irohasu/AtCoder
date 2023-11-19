# A問題
S, T = input().split()
san = "san"
print(S, san)


# B問題
n = int(input())
cnt = [0 for _ in range(24)]
for i in range(n):
    w, x = map(int, input().split())
    cnt[x] += w
    
ans = 0
for i in range(24):
    sum = 0
    for j in range(9):  # 9:00 ~ 17:00スタートの9通り
        sum += cnt[(i + j) % 24] # 例えば、標準時間が0時のとき、
    ans = max(ans, sum)          # 勤務時間の幅で最大人数を計算する、
print(ans)                       # これを24時間のそれぞれについてする



# C問題
from collections import deque

# 隣接するのは上下左右、斜めの８通り
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = 0
que = deque()
visited = [[False] * w for _ in range(h)]

# BFS
for i in range(h):
    for j in range(w):
        if s[i][j] == '.' or visited[i][j]:
            continue
        que.append((i, j))
        
        while que:
            y, x = que.popleft()
            
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if 0 <= ny < h and 0 <= nx < w and s[ny][nx] == '#' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    que.append((ny, nx))
        ans += 1

print(ans)


# D問題
import heapq
N = int(input())
TD = sorted([list(map(int, input().split())) for _ in range(N)])
TD.append([10 ** 20, 10 ** 20])
Q = []
Currenttime = 0
ans = 0

for t, d in TD:
    while Q and Currenttime < t:
        q = heapq.heappop(Q)
        if q >= Currenttime:
            ans += 1
            Currenttime += 1
    heapq.heappush(Q, t+d)
    Currenttime = t
print(ans)