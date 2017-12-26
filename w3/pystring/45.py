def stri45():
    a=input("Enter any string : ")
    
    b=""
    su=0
    for i in a.split():
        b+=i
    for i in range(65,91):
        if((chr(i) in a) or (chr(i).lower() in a)):
            su+=1
        else :
            print("NO, not all alphabets lies in the entered string : ")
            break
    if(su==len(b)):
        print("yes all alphabets lies in the entered string !")
        
    
        
