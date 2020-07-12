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

def m(a,e,m):
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
