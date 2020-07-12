def crt_list(primes, value):
    Mx=[]
    Yx=[]
    M=1
    cnt_p=len(primes) #The number of primes
    X=0

    for p in primes:
        M=M*p

    for p in primes:
        Mx.append(int(M/p))

    for i in range(0,cnt_p):
        j=1        
        while 1:
            if Mx[i] * j % primes[i] == 1:
                Yx.append(j)
                break
            else:                
                j=j+1      

    for i in range(0,cnt_p):
        X=X+value[i]*Mx[i]*Yx[i]

    return X%M
