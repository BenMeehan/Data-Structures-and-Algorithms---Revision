li=[1,2,3,4,5,3]

# def get(li,i,k):
#     if len(li)==0:
#         return -1 
#     if li[-1]==k:
#         return i 
#     return get(li,i-1,k)

# print(get(li,len(li)-1,3))

def get(li,k):
    if len(li)==0:
        return -1
    r=get(li[1:],k)
    if r!=-1:
        return r+1 
    else:
        if li[0]==k:
            return 0 
        else:
            return -1


print(get(li,3))