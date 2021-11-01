s=input()

def check(s):
    if len(s)==0 or len(s)==None:
        return True
    if len(s)==1:
        if s[0]=='a':
            return True
        else:
            return False 
    if len(s)==2:
        return False 
    
    return (s[0]=='a' and s[1]=='b' and s[2]=='b') and check(s[3:])

print(check(s))