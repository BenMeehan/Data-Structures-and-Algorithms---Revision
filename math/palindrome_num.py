n=int(input())

rev=0

while n>0:
    digit=n%10
    rev=rev*10+digit 
    n=n//10

if n==rev:
    print("yes")
else:
    print("no")