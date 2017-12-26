def tupli():
    su=0
    s= [(2,5),(1,2),(4,4),(2,3),(2,1)]
    for i in range(len(s)):
        for j in range(len(s)-1):
            if(s[j][1]>s[j+1][1]):
                s[j],s[j+1]=s[j+1],s[j]
                su+=1
            else:
                pass
        if(su==0):
             break
    print(s)
    
