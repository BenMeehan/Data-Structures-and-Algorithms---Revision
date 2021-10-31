li=[12,2,4,5]

def find(li,k):
    if len(li)==0:
         return False
    if li[0]==k:
        return True 
    return find(li[1:],k)

print(find(li,29))