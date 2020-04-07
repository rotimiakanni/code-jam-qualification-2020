# question 3

ip = open('file3.txt', 'r')
ran = int(ip.readline())
for x in range(ran):
    ans = ''
    C = 0
    J = 0
    nxt_ran = int(ip.readline())
    for y in range(nxt_ran):
        activ = [int(o) for o in ip.readline().split()]
        if y == 0:
            ans += 'C'
            C = activ[1]
        else:
            if activ[0] < C and activ[0] >= J:
                ans += 'J'
                J = activ[1]
            elif (activ[0] < J or J == 0) and activ[0] >= C:
                ans += 'C'
                C = activ[1]
            elif C < activ[0] and J < activ[0]:
                ans += 'C'
                C = activ[1]
            elif activ[0] < C and activ[0] < J:
                ans = 'IMPOSSIBLE'
                for u in range(nxt_ran - 1 - y):
                    bad = ip.readline()
                break

    print('Case #' + str(x + 1) + ': ' + ans)
