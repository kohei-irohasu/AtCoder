# A問題
b, g = map(int, input().split())
print('Bat' if b > g else 'Glove')


# B問題
# LからRみたいな問題は累積和の利用を考える。
# それぞれmがどれだけあるか考える。
a, m, l, r = map(int, input().split())

r -= a
l -= a
print(r // m - (l - 1) // m)


# C問題
# 数直線で考える。
# そろっている靴下はそのまま組み合わせるのが最適解。
# 靴下の数が偶数と奇数で場合分け。
# 偶数の場合、かけているものは小さい順に組み合わせる。
# 奇数の場合、欠けているものの中でどれを余らせるか考える。
# このとき、偶数は考えなくてよいため、奇数のみを余らせたときの最小値を求める。
# はじめのnowはa0を余らせた場合で、以降のループでa2, a4と続いていく。
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
if k % 2 == 0:
    for i in range(1, k, 2):
        ans += a[i] - a[i - 1]
    print(ans)
else:
    now = 0
    for i in range(2, k, 2):
        now += a[i] - a[i - 1] # a0を余らせたとき
    ans = now
    for i in range(2, k, 2):
        now += a[i - 1] - a[i - 2] # nowはどんどん更新されていく
        now -= a[i] - a[i - 1]
        ans = min(now, ans)
    print(ans)

