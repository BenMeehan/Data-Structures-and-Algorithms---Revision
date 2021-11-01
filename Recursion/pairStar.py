s=input()

def pairStar(s):
    if len(s)==1:
        return s 
    return s[0]+"*"+pairStar(s[1:])

print(pairStar(s))