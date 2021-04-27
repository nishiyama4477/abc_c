n = int(input())
a_s = [] # 人のリスト
q_s = [] # 返答のリスト
for i in range(n):
    a = int(input())
    a_s.append(0)
    for q in range(a):
        p_and_boo = []
        person, boo = map(int, input().split())
        p_and_boo.append(person)
        p_and_boo.append(boo)
        q_s.append(p_and_boo)

print(a_s, q_s)

# 証言をコード化する →一人目の証言だったら、h_or_l[1] == 1みたいに

new_a_s = []
for i, w in enumerate(q_s):
    new_a_s.append(str(w[0]) + 'は' + str(w[1])) # まだ出来ていない。コード化しなければ

print(new_a_s) # 2**nのそれぞれのパターンに関してnew_a_sが当てはまるか。つまり2**nループの中にnew_a_sループ

# counts = []
#
# for j in range(2**n):
#     h_or_l = [0] * n
#     for w in range(n):
#         if ((j>>w) & 1):# この条件に当てはまる人は正解者（もしくは嘘つき）←どっちでもいい。 矛盾を見つけるには正直者の発言が正しいかどうか。矛盾していればこの中には正直者がいない
#             h_or_l[w] = 1
#     print(h_or_l)
#
#     count = 0
#     for i in h_or_l:
#         if i  == 1:
#             count += 1
#     print("countは" + str(count))

