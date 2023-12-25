# A問題
n = input()
print(n * int(n))


# B問題
# 辺の長さの種類は２種類のみ。
# 短い = 隣接している。
s = input()
t = input()
chr = 'ABCDEAEDCBA'
if (s in chr and t in chr) or (not s in chr and not t in chr):
    print('Yes')
else:
    print('No')