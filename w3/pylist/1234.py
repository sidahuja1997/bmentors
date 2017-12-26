def asmm(a):
    su=0
    dif=1
    ma=0
    
    mi=a[0]
    for i in a:
        
        su+=i
        dif*=i
        if(ma<i):
            ma=i
        if(mi>i):
            mi=i
    print("sum is %i\nproduct is %i\nmaximum is %i\nminimum is %i"%(su,dif,ma,mi))
    
