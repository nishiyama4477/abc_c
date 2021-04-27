n, m = map(int, input().split())

a_list = []
b_list = []

corrects = 0
penalties = 0

for i in range(m):
    a, b = map(str, input().split())
    if a_list != [] and a not in a_list:
         print('決算！')
         print('a_listは', a_list)
         print('b_listは', b_list)
         if 'AC' in b_list:
             corrects += 1
             print('added to CORRECTS')
         if 'WA' in b_list:
             penalties += 1
             print('added to PENALTIES')
         a_list.clear()
         b_list.clear()
         a_list.append(a)
         b_list.append(b)
    else:
        print('pass')
        a_list.append(a)
        b_list.append(b)
        print('a_listは', a_list)
        print('b_listは', b_list)
        if i == m - 1:
            print('last処理')
            if 'AC' in b_list:
                corrects += 1
                print('added to CORRECTS')
            if 'WA' in b_list:
                penalties += 1
                print('added to PENALTIES')


print(corrects, penalties)
