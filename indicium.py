ip = open('file4.txt', 'r')

for sample in range(int(ip.readline())):
    sqr_mat, diag = [int(x) for x in ip.readline().split()]
    thresh = sqr_mat ** 2
    mat_lis = []
    
    for x in range(sqr_mat):
        mat_lis.append(x + 1)
    if sqr_mat % 2 == 1:
        if diag % sqr_mat == 0 and diag <= thresh:
            diag_val = int(diag / sqr_mat)
            print(diag_val)
            mat_ans = []
            for ma in range(sqr_mat):
                temp_list = []
                deal = mat_lis.index(diag_val) - sqr_mat
                deal -= ma
                if deal < -sqr_mat:
                    deal += sqr_mat
                print(deal)
                for y in range(sqr_mat):
                    temp_list.append(mat_lis[deal])
                    deal += 1
                    print(temp_list)
                mat_ans.append(temp_list)
            print('CASE #' + str(sample) + ': '+'POSSIBLE')
            for x in mat_ans:
                for y in x:
                    print(str(y), end=' ')
                print('\n')
        else:
            print('CASE #' + str(sample) + ': '+'IMPOSSIBLE')
    else:
        temp_hold = sqr_mat / 2
        if diag % sqr_mat == 0 and diag <= thresh:
            diag_val = diag / sqr_mat
            mat_ans = []
            
            for x in range(sqr_mat):
                temp_list = []
                deal = mat_lis.index(diag_val) - sqr_mat
                deal -= ma
                print(deal)
                for y in range(sqr_mat):
                    temp_list.append(mat_lis[deal])
                    deal += 1
                mat_ans.append(temp_list)
            print('CASE #' + str(sample) + ': '+'POSSIBLE')
            for x in mat_ans:
                for y in x:
                    print(str(y), end=' ')
                print('\n')
#        elif diag == (sqr_mat * (sqr_mat/2)) + (sqr_mat/2) and diag <= thresh:
#            print('CASE #' + str(sample) + ': '+'POSSIBLE')
#            nxt = []
#            for i in range(sqr_mat):
#                nxt.append([j for j in range(srq_mat)])
#            for u in range(sqr_mat):
#                for v in range(sqr_mat):
#                    if u == v:
#                        nxt[u][v] = u+1
#                    else:
                        
                    
        else:
            print('CASE #' + str(sample) + ': '+'IMPOSSIBLE')
