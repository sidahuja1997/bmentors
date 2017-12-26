def l35(n):
    l=[2]
    for i in range(3,n+1):
        su=0
        for j in l:
            if(i%j==0):
                su+=1
                break
        if(su==0):
            l+=[i]
    print(l)
    
