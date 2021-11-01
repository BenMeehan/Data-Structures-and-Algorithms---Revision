n=int(input())

def count(n):
    if n==0:
        return 0
    
    dig=n%10
    sm=count(n//10)

    if dig==0:
        return 1+sm 
    else:
        return sm

print(count(n))