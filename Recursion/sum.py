li=[1,2,3,4,5]

def summ(li):
    if len(li)==1:
        return li[0]
    return li[0]+summ(li[1:])

print(summ(li))