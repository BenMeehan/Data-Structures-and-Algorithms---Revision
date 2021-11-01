s=input()

def removex(s):
    if len(s)==0 or len(s)==1:
        return s 
    if s[0]==s[1]:
        return s[0]+removex(s[2:])
    else:
        return s[0]+removex(s[1:])

print(removex(s))