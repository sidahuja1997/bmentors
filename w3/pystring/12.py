def stri12():
    a=input("enter a string  : ")
    a=a.split()
    
    d=dict()
    for i in a:
        su=0
        for j in a:
            if(j==i):
                su+=1
            
        d[i]=su
    print(d)
    for i in d.keys():
        print('%s is %i times used'%(i,d[i]))
        
        
    
