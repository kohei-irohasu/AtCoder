# A問題
b, g = map(int, input().split())
print('Bat' if b > g else 'Glove')


# B問題
# LからRみたいな問題は差を考える。
# それぞれmがどれだけあるか考える。
a, m, l, r = map(int, input().split())

r -= a
l -= a
print(r // m - (l - 1) // m)
