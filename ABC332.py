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