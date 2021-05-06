# ポイント①: WAはACが出るまで、ACは一つの問題につき一つだけ→つまり,ACが出た時点で次の問題に移る
# 検証1：　問題が変わればac_cntとwc_cntを0にリセット
#         ACかつac_cntが0であればac += 1,wc += wc_cnt
#         WCかつac_cntが0であればwc_cnt += 1

n, m = map(int, input().split())

sth = 'dammy'
ac = 0
wc = 0
wc_cnt = 0
ac_cnt = 0

for i in range(m):
    a, b = map(str, input().split())
    if a != sth:
        # print('switched!')
        wc_cnt = 0
        ac_cnt = 0
        sth = a

        if b == 'AC':
            ac_cnt += 1
            # print('ac_cnt += 1')
            ac += 1
            # print('ac += 1')
        else:
            wc_cnt += 1
            # print('wc_cnt += 1')

    else:
        if b == 'AC':
            if ac_cnt == 0:
                ac_cnt += 1
                # print('ac_cnt += 1')
                ac += 1
                # print('ac += 1')
                wc += wc_cnt
                # print('wc += wc_cnt')
        else:
            if ac_cnt == 0:
                wc_cnt += 1
                # print('wc_cnt += 1')

print(ac, wc)