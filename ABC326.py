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
