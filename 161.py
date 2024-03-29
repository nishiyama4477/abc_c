# 例の３から分かるようにただforループしてもならない。
# 一つ気づいた事として原点を跨ぐ時は数値が固定される
#  例えば, n=7, k=4の時、2thのoperationでabs(3-4)=1、3thのoperationでabs(1-4)=3、4thのoperationでabs(3-4)=1
# 上記の例+n=100000000000000である可能性があることを考えれば、”原点を跨ぐまでの範囲で、おおよその見切りを付けられるプログラムを書く必要がある。”
# ①if文一つ目：nがkで割り切れれば答えは0
# ②else文は下記
# n = 7, k = 4の時、k=4を使って表すと n = 4*1 +3  原点を跨ぐとき値は3か１を取る
# n = 2, k = 6の時、k=6を使って表すと n = 6*1 -4　原点を跨ぐとき値は4か2を取る
# n = 13, k = 4の時、k=4を使って表すと n = 4*3 +1　原点を跨ぐとき値は1か３を取る
# 上記の式の余りの部分をmとすると、取りうる値は m or k-mであることが分かる。つまりそれぞれのinputに対して m と k-mで小さい方が答えになるのではないか
# また、原点を跨ぐまでのforの数はn/kである。

n, k = map(int, input().split())

if n % k == 0:
    print(0)
    # exit()
elif n > k:
    remain = n - k * (n//k)
    # print(remain)
    print(min(remain, k-remain))
elif n < k:
    remain = n - k * 1
    # print(remain)
    print(min(abs(remain), k-abs(remain)))


