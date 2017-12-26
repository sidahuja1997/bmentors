def remd(l):
    
    d={}
    for i in l:
        su=0
        for j in l:
            if(j==i):
                su+=1
        d[i]=su
    for i in d.keys():
        for k in range(d[i]-1):
            l.remove(i)
            
    print(l)
    
