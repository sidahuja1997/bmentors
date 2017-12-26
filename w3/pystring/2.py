def stri2():
    a=input("enter a string : ")
    d=dict()
    
    for i in a:
        su=0
        for j in a:
            if(j==i and i not in d.keys()):
                su+=1
        if(su!=0):
            d[i]=su

    print(d)
    

