def l27(l):
    minn=l[0]
    print(minn)
    for i in range(1,len(l)):
        if(l[i]<minn):
            minn=l[i]
            
    l.remove(minn)
    mi=l[0]
    for i in range(1,len(l)):
        if(l[i]<mi):
            mi=l[i]
    print(mi," is the second lowest value ")
    
    
    
