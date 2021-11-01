s=input()

def convert(s):
    if len(s)==0:
        return 0
    return (ord(s[0])-48)*pow(10,len(s)-1)+convert(s[1:])
    
    
print(convert(s),type(convert(s)))