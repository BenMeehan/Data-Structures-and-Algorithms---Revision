import random
def partition(li,si,ei):
    idx=random.randint(si,ei)
    li[si],li[idx]=li[idx],li[si]
    pi=si
    i,j=si,si+1

    while j<=ei:
        if li[j]<li[pi]:
            i+=1 
            t=li[i]
            li[i]=li[j]
            li[j]=t
        j+=1
    t=li[i]
    li[i]=li[pi]
    li[pi]=t
    return i

def quickSort(li,si,ei):
    if si>=ei:
        return 
    pi=partition(li,si,ei)
    quickSort(li,si,pi-1)
    quickSort(li,pi+1,ei)

arr=[5,4,1,2,8,6]
quickSort(arr,0,len(arr)-1)
print(arr)