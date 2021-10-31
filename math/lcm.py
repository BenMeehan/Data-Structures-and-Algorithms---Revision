a=int(input())
b=int(input())

def gcd(a,b):
    if b==0:
        return a 
    else:
        return gcd(b,a%b)

lcm=(a*b)//gcd(a,b)
print(lcm)