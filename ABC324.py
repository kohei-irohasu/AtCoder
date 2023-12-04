# A問題
N = int(input())
A = set(map(int, input().split()))
print('Yes'if len(A) == 1 else 'No')


# B問題
N = int(input())

while N % 2 == 0:
    N //= 2
while N % 3 == 0:
    N //= 3

print('Yes' if N == 1 else 'No')


# C問題
def check(s, t):
    if len(s) > len(t): 
        return check(t, s)  # 常に s<t としておく
    if len(s) < len(t) - 1: # 差が2以上だったらアウト
        return False
    i, j, miss = 0, 0, 0
    while i < len(s):
        if s[i] == t[j]: # 先頭から1文字ずつ見ていく
            i += 1
            j += 1
        else:
            miss += 1
            if miss > 1: # 相違点は2以上だったらアウト
                return False
            if len(s) == len(t):
                i += 1
            j += 1
    return True

N, T = input().split()
N = int(N)
ans = []
for i in range(N):
    S = input()
    if check(S, T):
        ans.append(i + 1)
print(len(ans))
print(" ".join(map(str, ans))) # 文字列でないと、joinできない


# D問題
N = int(input())
S = input()
S = ''.join(sorted(S)) # Sをsortしておく

max_value = 10 ** N
ans = 0

for i in range(int(max_value ** 0.5) + 1):
    T = str(i * i) # 平方数
    T = T.zfill(N) # 桁数をそろえる
    T = ''.join(sorted(T)) #　sortして
    if S == T:
        ans += 1
        
print(ans)