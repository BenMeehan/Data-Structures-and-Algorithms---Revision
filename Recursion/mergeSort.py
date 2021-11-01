def mergeSort(li):
    if len(li)==None or len(li)<=1:
        return li
    mid=len(li)//2
    l=mergeSort(li[:mid])
    r=mergeSort(li[mid:])
    li=merge(l,r)
    return li


def merge(l,r):
    new=[]
    m,n=len(l),len(r)
    i,j=0,0
    while  i<m and j<n:
        if l[i]<r[j]:
            new.append(l[i])
            i+=1
        else:
            new.append(r[j])
            j+=1

    while i<m: 
        new.append(l[i])
        i+=1

    while j<n:
        new.append(r[j])
        j+=1
    return new

li=[2,5,1]
li=mergeSort(li)
print(li)