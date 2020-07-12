import random
import hashlib

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

def gcd(a,b):
    while(1):
        r=a%b
        a=b
        b=r
        if r==0:
            return a
        
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


def generate_prime_subgroup (plen, qlen):
     #generate primes p and q
     while 1:
          q=random.randint(2, 2**qlen)
          if(is_prime(q)):
               break
          
     while 1:
          k=random.randint(2, 2**(plen-qlen))
          if(is_prime(k*q+1)):
               p=k*q+1
               break

     #g is a^k mod p
     a=random.randint(2, p-1)
     g=mod_exp(a,k,p)

     param=(p, q, g)
     return param

def schnorr_setup(plen):
     #return pp which contains (p, q, g)
     pp=generate_prime_subgroup(plen,160)
     return pp

def schnorr_genkey(pp):
     # pp contains (p, q, g)
     # sk is random a
     sk=random.randint(0, pp[1]-1)

     # pk is b=g^a mod p 
     pk=mod_exp(pp[2], sk, pp[0])
     return sk, pk

def hex_to_int(hexi):
    result = 0
    for b in hexi:
         result = result*16 + int(b, base=16)
    return result

def schnorr_hash(R, msg, q):
     Bi_R = ''.join(format(ord(x), 'b') for x in str(R))
     Bi_msg=''.join(format(ord(x), 'b') for x in msg)
     Bi=Bi_R + Bi_msg

     h = hashlib.sha1(Bi.encode('utf-8'))
     
     # h is H(R || m)
     h = hex_to_int(h.hexdigest())%q
     return h

def schnorr_sign(msg, sk, pp):
     # sk is a
     # pp contains (p, q, g)
     k=random.randint(1,pp[1]-1)
     R=mod_exp(pp[2], k, pp[0])
     h=schnorr_hash(R, msg, pp[1])

     s=(k+sk*h) % pp[1]
     sig=(R, s, h)
     return sig

def schnorr_verify(sig, msg, pk, pp):
     # sig contains (R, s, h, k)
     # pk is b
     # pp contains (p, q, g)
     
     y=mod_exp(pp[2], sig[1], pp[0])
     
     Ax= sig[0]
     Bx=mod_exp(pk, sig[2], pp[0])
     x=sig[0]*Bx % pp[0]

     print("y={}\nx={}".format(y,x))
     
     if(y == x):
          return 1
     else:
          return 0
