def list5(a):
    su=0
    for i in a:
        if((i[0]==i[len(i)-1]) and len(i)>=2):
            su+=1
    print("The number of strings with first and last letter same and length over 2 are %i"%(su))
    
