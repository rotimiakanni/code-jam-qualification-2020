import numpy as np

ip_file = open('file.txt', 'r')
p = int(ip_file.readline())
for mats in range(p):
    diag = 0
    sqr_mat = int(ip_file.readline())
    row_count = 0
    col_count = 0
    mat = []
    for x in range(sqr_mat):
        row = ip_file.readline().split()
        diag += int(row[x])
        for x in row:
            if row.count(x) > 1:
                row_count += 1
                break
        mat.append(row)
    arr = np.array(mat)
    arr = arr.transpose()
    arr = arr.tolist()
    print(arr)
    for x in arr:
        for y in x:
            if x.count(y) > 1:
                col_count += 1
                break
            
    print('Case #' + str(mats + 1) + ':' + str(diag) + ' ' + str(row_count) + ' ' + str(col_count))
