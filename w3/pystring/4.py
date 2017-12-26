def stri4():
    a=input("enter a string : ")
    b=""
    a=a.split(" ")
    for i in a:
        print(i)
        for j in range(0,len(i)):
           
            if(i[j]==i[0] and j!=0):
                b+="$"
            else:
                b+=i[j]
                
        b+=" "
    print(b)
    

    
