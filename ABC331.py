# A問題
M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d == D:
    d = 1
    if M == m:
        m = 1
        y += 1
    else:
        m += 1
else:
    d += 1

print(y, m, d)


# B問題
n, s, m, l = map(int, input().split())
ans = 10 ** 6

for i in range(18):
    for j in range(18):
        for k in range(18):
            if  6 * i + 8 * j + 12 * k >= n:
                ans = min(ans, i * s + j * m + k * l)
print(ans)