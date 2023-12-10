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

