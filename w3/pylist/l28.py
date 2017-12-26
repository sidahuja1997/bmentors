def l28(l):
    maxx=l[0]
    print(maxx)
    for i in range(1,len(l)):
        if(l[i]>maxx):
            maxx=l[i]
            
    l.remove(maxx)
    maxx=l[0]
    for i in range(1,len(l)):
        if(l[i]>maxx):
            maxx=l[i]
    print(maxx," is the second highest value ")
    
    
    
