def l26():
    n=int(input("Enter the number for elements in list : "))
    l=[]
    b=[]
    su=0
    for i in range(n):
        b+=[int(input("Enter the number : "))]
        l+=[int(input("Enter the number : "))]
    for i in range(len(l)):
        if(l==b):
            print("The list are circularly identical !")
            break
        else:
            a=l.pop()
            l+=[a]+l
            su+=1
    if(su==len(l)):
        print("The lists are not circularly identical!")

        
