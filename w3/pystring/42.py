def stri42():
    a=input("Enter a string : ")
    a=list(a)
    a.sort()
    d={}
    for i in a:
        su=0
        for j in a:
            if(j==i):
                su+=1
            d[i]=su
    print(d)
    for i in d.keys():
        if(d[i]!=1):
            print("%s\t\t%i"%(i,d[i]))
            
            
                
