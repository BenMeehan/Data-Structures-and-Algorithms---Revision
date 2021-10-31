li=[1,2,3,4,5,3]

def get(li,i,k):
    if len(li)==0 or i==len(li):
        return -1
    if li[i]==k:
        return i
    else:
        return get(li,i+1,k)

print(get(li,0,1))