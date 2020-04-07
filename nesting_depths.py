# Question 2
ip = open('file2.txt', 'r')
ran = int(ip.readline())
for x in range(ran):
    op = 0
    cl = 0
    mi = 0
    ans = ''
    sample = ip.readline().strip()
    for p in range(len(sample)):
        y = int(sample[p])
        
        if y > mi:
            ans += ('(' * (y-mi))
            op += (y-mi)
            ans += str(y)
            mi = op - cl
        elif y < mi:
            cl += (mi - y)
            ans += (')' * (mi - y))
            ans += str(y)
            mi = op - cl
        elif y == mi:
            ans += str(y)
        if p == len(sample) - 1:
            ans += (')' * mi)
        
    print('Case #' + str(x+1) + ': ' + ans)
