def crt (p,q,a,b):
    M1=q
    M2=p
    i=1
    M=p*q
    flag = 0
    
    while 1:
        if M1*i%p == 1:
            Y1=i
            break
        else:
            i=i+1
    if i > 0:
        flag = 1
    i=1
    while 1:
        if M2*i%q == 1:
            Y2=i
            break
        elif M2*i%q != 1 & flag == 1:
            i=i-1
        else:
            i=i+1
    x=a*M1*Y1 + b*M2*Y2
    return x%M
