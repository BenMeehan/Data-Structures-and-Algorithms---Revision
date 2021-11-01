n=int(input())

def climb(n):
    if n==0 or n==1:
        return 1 
    if n==2:
        return 2
    
    return climb(n-1)+climb(n-2)+climb(n-3)

print(climb(n))