def l14():
    l=[]
    b=[]
    c=[]
    for i in range(3):
        for j in range(4):
            for k in range(6):
                c+=["*"]
            b+=[c]
        l+=[b]
    print(l)
    
