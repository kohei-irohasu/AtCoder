# A問題
n, l = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in a:
    if i >= l:
        ans += 1

print(ans)   


# B問題
n, l, r = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in a:
    if i < l:
        ans.append(l)
    elif i <= r:
        ans.append(i)
    else:
        ans.append(r)

print(*ans)


# C問題
# 全探索
# xの範囲は、0<= x <= x ** 0.5
# xが決まるとyも定まるので、ありえる全ての値について計算していく。
d = int(input())
ans = d
for i in range(int(d ** 0.5) + 1):
    j = int((d - i ** 2) ** 0.5)
    ans = min(ans, 
              abs(d - i ** 2 - j ** 2),
              abs(d - i ** 2 - (j + 1) ** 2))
print(ans)