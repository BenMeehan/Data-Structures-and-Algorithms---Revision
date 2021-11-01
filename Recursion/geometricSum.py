def gSum(a,r,n):
    if n==0:
        return 1
    else:
        return a*pow(r,n)+gSum(a,r,n-1)

print(gSum(1,2,4))