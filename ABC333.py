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
    

# C問題
# 答えとしてあり得る値を全探索。
# 各桁は1 ~ 3、単調増加、1の位は3。
# d: 何桁のレピュニットか。
# 小さい順に数える、単調増加だから、
# d,a,b,cの順でループ。
n = int(input())
for d in range(1, 13):
    for a in range(d - 1, -1, -1):
        for b in range(d - a - 1, -1, -1):
            c = d - a - b
            n -= 1
            if n == 0:
                result = '1' * a + '2' * b + '3' * c
                print(result)
                
# 別解
# sampleから最大でも12桁。
# 重複ありの場合のループ文の回し方。
n = int(input())
l = 12
r = [int('1' * (i + 1)) for i in range(l)]
for i in range(l):
    for j in range(i + 1):
        for k in range(j + 1):
            n -= 1
            if n == 0:
                print(r[i] + r[j] + r[k])