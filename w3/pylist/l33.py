def l33(l):
    b=[[]]
    for i in range(len(l)):
        n=i+1
        while(n<=len(l)):
            b.append(l[i:n])
            n+=1
    return b
