# A問題
S = input()
if S[1::2] == '0' * 8:
    print('Yes')
else:
    print('No')
    
    
# B問題
#　入力を受け取る
N  = int(input())
S = [input() for _ in range(N)]

# 各プレイヤーについて勝ち数を求める
wins = [0] * N
for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            wins[i] += 1

bucket = [[] for _ in range(N)]
for i in range(N):
    bucket[wins[i]].append(i) # 勝ち数のところにプレイヤー番号を入れる
    
ans = []
for i in range(N - 1, - 1, - 1):  #　小さい順に並んでいるので後ろから
    for j in bucket[i]:           # bucket[i]にはプレイヤー番号が入っている
        ans.append(j + 1)

print(*ans)


# C問題
# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

# 各プレイヤーの現在の総合得点
score = [0] * N
for i in range(N):
    for j in range(M):
        if S[i][j] == 'o':
            score[i] += A[j]
    score[i] += i + 1

# 各プレイヤーについて、解いていない問題を点数の降順に
# 並べ替え、ほかのプレイヤーより高くなるまで問題を解いていく
max_score = max(score)
for i in range(N):
    rest_ques_score = [A[j] for j in range(M) if S[i][j] == 'x']
    rest_ques_score.sort(reverse=True)
    ans = 0
    while score[i] < max_score:
        score[i] += rest_ques_score[ans]
        ans += 1
    print(ans)
    

# D問題
# スライムを割れるだけ割る。最終的に0か1。
# set()でサイズを管理。
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

kind = set()
for s, c in data:
    while c >= 1:
        if s in kind:  # kindにあったら、数を+1して、kindから削除
            c += 1
            kind.discard(s)
        if c == 1:     # 1っ匹だったら、kindに追加
            kind.add(s)
            break
        if c % 2 == 1: # 奇数だったら追加
            kind.add(s)
        c //= 2   # 新しく生成されるスライムの数
        s *= 2    # 新しく生成されるスライムの大きさ

print(len(kind))