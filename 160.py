# 仮説
# 最短とは”一周すること”
# 円で考えると、①最長となる2点間を発見して、②その後反対側を取ればいい
# 家の位置はclockwiseで、たどり方はどっちでもいい。
# また池の長さが⑳の時、0と15間で、距離は15にもなり得るし(clockwise)、5にもなり得る(anticlockwise)。
# 原点を挟んだ時の距離を考える。この原点はkとなる。
# mostを考えれば良くて、それはclockwiseで見つける。clockwiseでそれぞれの長さを調べた時に一番長いのがmost
# mostが見つかれば後は逆に○を描く時の長さを見つければ良い。

k, n = map(int, input().split())
As = list(map(int, input().split()))

# とりまinput3つに対してoutput3つ出す関数を作りたい(a,b,c点が与えられれば(input)、AB,BC,CAの長さを返す(output)。このときclockwiseである。

for i in As:
    print(i)