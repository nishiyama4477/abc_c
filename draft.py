# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC165
# 仮説１
# ステップを分けると、①Aのとりうる値を決める。②点数を判定し、より大きければ更新。←でも多分①の段階でおおよそのとりうる値的なのは見つけられそう。
# というより、Asからある程度数字を予測できそうな気もする。=cになるようにAを作れば良いだけ。
# 組み合わせの考え方を使えばいけそう。
# 2月13日の考え方。
# ①条件からそれぞれの値の候補を見つける。②条件から絞られた候補の中で組み合わせていく。
# 2月17日更新
# 多分これはbit全探索や。おそらく①まずbit全探索でパターンを網羅する。②それぞれのパターンについて条件を満たす数字が存在するか調べる。


n, m, q = map(int, input().split())
quads = []

for i in range(q):
    quad = list(int(i) for i in input().split())
    quads.append(quad)

print(quads)

N = len(quads)

most = 0

for i in range(2**N):
    pattern = []
    print('pattern{}:'.format(i))
    for j in range(N):
        if (i >> j) & 1:
            pattern.append(quads[j])
            base = m - quads[j][2]
            for s in range(0, base):
                b = m - s
                a = s+1



    print(pattern)





    # if result >= most:
    #     most = result




#　↑このquadsに関してbit全探索でパターンを網羅する。


















#
# opt = [list() for i in range(n)]
# print(opt)
#
# As = []
#
# for s in range(q):
#     print('===================')
#     a = list(int(i) for i in input().split())
#     # 引かれる数のindex値は
#     frm_ind = a[1]
#     print('引かれる数のindexは', frm_ind)
#     # 引く数のindex値は
#     sub_ind = a[0]
#     print('引く数のindexは', sub_ind)
#
#     frm = []
#     subtracted = []
#     # nからcを引いた数
#     howmany = n - a[2]
#     print('howmany is', howmany)
#
#     #引かれる数の候補を用意
#     for i in range(0, howmany+1):
#         frm.append(n-i+1)
#     print('frm is', frm)
#
#     #引く数の候補を用意
#     for i in range(0, howmany+1):
#         subtracted.append(i+1)
#     print('subtracted is', subtracted)
#
#     opt[frm_ind-1] += frm
#     opt[sub_ind-1] += subtracted
#
#     print('opt is', opt)
#     # subtracted =
#     As.append(a)
#
# print(As)



