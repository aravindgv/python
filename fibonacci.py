def fibonacci(n):
    #a,b = 0,1
    a=0
    b=1
    while a < n:
        print a,
        #a=b
        #b=a+b
        a,b = b,a+b

fibonacci(100)