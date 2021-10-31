li=[1,2,3,4,5,8,7]

def isSorted(li,si):
    if si>=len(li)-1:
        return True
    if li[si]>li[si+1]:
        return False
    else:
        if isSorted(li,si+1):
                return True 
        else:
                return False
print(isSorted(li,0))