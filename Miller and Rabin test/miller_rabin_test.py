def mod_exp(a,e,m):
     bi=[] #이진수 
     sum=1
     while e!=0:
        bi.append(e%2)
        e=int(e/2)
     t=a
     for i in bi:
         if i==1:
             sum=sum*t%m
         t=t**2%m
     return sum

def miller_test(n,b,s,t):
    flag=0
    e=t/2
    for i in range(0,s):
        e=int(e*2)
        res=mod_exp(b,e,n)
      #  print("res={}".format(res))
        if not flag:
            if(res==1 or res==-1):
                return 1
            flag=flag+1
        else:
            if(res==-1):
                return 1
            elif (res==1):
                return 0
    return 0  
