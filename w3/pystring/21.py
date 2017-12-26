def stri21():
    a=input("enter a string : ")
    su=0
    b=""
    for i in a:
        if(i==i.upper()):
            su+=1
    if(su>2):
        for i in a:
            b=i+b
    print(b)
    
