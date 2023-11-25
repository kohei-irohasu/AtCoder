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