def gcd(a,b):
    while(1):
        r=a%b
        a=b
        b=r
        if r==0:
            return a

def extended_gcd(a,b):
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
            #where a is division 'd'
            return a, s0,t0

def print_extended_gcd(dst):
    print("d:{}, s:{}, t:{}".format(dst[0],dst[1],dst[2]))

print_extended_gcd(extended_gcd(45,78))
print_extended_gcd(extended_gcd(666,1428))
print_extended_gcd(extended_gcd(1020,10290))
print_extended_gcd(extended_gcd(2**20+4,3**10+5))
print_extended_gcd(extended_gcd(2**30+1,3**30+6))
