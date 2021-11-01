def toh(n,source,helper,dest):
    if n==1:
        print("Move disc "+str(n)+" from "+source+" to "+dest)
        return
    toh(n-1,source,dest,helper)
    print("Move disc "+str(n)+" from "+source+" to "+dest)
    toh(n-1,helper,source,dest)

toh(2,'A','B','C')