for num in range(2,10):
    for x in range(2,num):
        if num % x == 0:
            #print num, 'equals',x, '*',num/x
            break
    else:
        print "prime numbers are",num
