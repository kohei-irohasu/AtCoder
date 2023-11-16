# A問題
X, Y = map(int, input().split())
print('Yes' if - 3 <= Y - X <= 2 else 'No')


# B問題
N = int(input())

for i in range(N , 920):
    digit3 = i // 100
    digit2 = (i // 10) % 10
    digit1 = i % 10
    
    if digit3 * digit2 == digit1:
        print(i)
        break


# C問題
N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A.append(10 ** 10) # l = N - 1のとき、r += 1が実行されてしまうため、
                   # Aのリストを１つ大きくしておく
res = 0
r = 0
for l in range(N):          # lについて全探索、rには最大の個数が入っているの
    while A[r] < A[l] + M:  # rは初期化しなくてよい
        r += 1
    res = max(res, r - l)

print(res)   



# D問題
# 深さ優先、再帰関数ver
# 各行の最後の列から、文字を埋めていく
def dfs(y, x, a, row, cols):
    # グリッドの各セルが埋まっている場合
    if y == N:
        # 列ごとに文字がA, B, Cで構成されているかチェック
        if all("".join(sorted(cols[j])) == "ABC" for j in range(N)):
            print("Yes")
            # グリッドの内容を表示
            print("\n".join("".join(row) for row in a))
            # プログラム終了
            exit(0)
    # 各行の最後の列まで到達した場合
    elif x == N:
        # 行ごとに文字がA, B, Cで構成されているかチェック
        if "".join(sorted(row)) == "ABC":
            # 次の行を埋めるために再帰呼び出し
            dfs(y + 1, 0, a, [], cols)
    # グリッドの中間部分に文字を埋めていく
    else:
        # 現在のセルを埋めずに次の列へ
        dfs(y, x + 1, a, row, cols)
        # "ABC"から一つの文字を選び、条件を満たすかどうかを判定してからセルを埋める
        for ch in "ABC":
            if row == [] and ch != R[y] or ch in row:
                continue
            if cols[x] == [] and ch != C[x] or ch in cols[x]:
                continue
            # グリッドの現在のセルにchを埋め、行と列のリストに追加
            a[y][x] = ch
            row.append(ch)
            cols[x].append(ch)
            # 次の列へ再帰呼び出し
            dfs(y, x + 1, a, row, cols)
            # 戻る前に埋めたセルを元に戻す
            a[y][x] = "."
            row.pop()
            cols[x].pop()

# 入力の取得
N = int(input())
R = input()
C = input()

# 初回のDFS呼び出し
dfs(0, 0, [["."] * N for _ in range(N)], [], [[] for _ in range(N)])

# 解が見つからなかった場合
print("No")
