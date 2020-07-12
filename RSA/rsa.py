import random

def mod_exp(a,e,m):
     bi=[] #이진수 
     sum=1
     while e!=0:
        bi.append(e%2)
        e=int(e//2)
     t=a
     for i in bi:
         if i==1:
             sum=sum*t%m
         t=t**2%m
     return sum

def me(a,e,m):
     bi=[] #이진수 
     sum=1
     while e!=0:
        bi.append(e%2)
        e=int(e//2)
     t=a
     for i in bi:
         if i==1:
             sum=sum*t%m
         t=t**2%m
     return sum

def m1(a,m):
     for j in range(0,5):
          for k in range(0,5):
               print("m={}, j={}, k={}".format(me(10, j+5*k,19), j, k))

def gcd(a,b):
    while(1):
        r=a%b
        a=b
        b=r
        if r==0:
            return a

def extended_gcd(a,b):
    Phi_n = b
    s0=1
    t0=0
    s1=0
    t1=1
    while(1):
        q=a//b #몫 연산자
        r=a%b
        a=b
        b=r
        
        s2=s0-q*s1
        t2=t0-q*t1
        s0=s1
        t0=t1
        s1=s2
        t1=t2
        if r==0:
            if (s0<0):
                s0+=Phi_n
                #where 's0' is 'd' in RSA
            return s0, t0
        
def miller_rabin_test(n,b,s,t):
    res=mod_exp(b,t,n)
    if(res==1 or res==n-1):
         return 1
    for i in range(1,s):
         res=res**2%n
         if (res==n-1):
              return 1
         elif (res==1):
              return 0
    return 0  

def is_prime(n):
     k=n-1
     s=0
     while 1:
          if k%2==0:
               s=s+1
               k=k//2
          else:
               t=k
               break
     
     for i in range(0,20):
          while 1:
               b=random.randint(2,n-1)
               if gcd(n,b)==1:
                    break
          if miller_rabin_test(n,b,s,t)==0:
               return 0
     return 1


def rsa_genkey(key_length):
    p_length = key_length/2
    q_length = key_length/2

    #generate large primes p and q and comput n=pq
    while 1:
        p=random.randint(2, 2**p_length)
        if(is_prime(p)):
            break
        
    while 1:
        q=random.randint(2, 2**q_length)
        if(is_prime(q)):
            break

    n=p*q
    
    #choose e with gcd(e,phi(n)) = 1 where phi(n) = (p-1)(q-1)
    Phi_n = (p-1)*(q-1)
    while 1 :
        e=random.randint(2, 2**p_length)
        if gcd(e, Phi_n) == 1:
            break
   
    #Compute d with ed = 1 mod Phi(n)
    d = extended_gcd(e, Phi_n)
    PK = (n, e)
    SK = (p, q, d)
    return SK, PK

def rsa_encrypt(m, pk):
    ct = mod_exp(m, pk[1], pk[0])
    return ct

def rsa_decrypt(ct, sk):
    n = sk[0] * sk[1]
    m = mod_exp(ct, sk[2], n)
    return m

