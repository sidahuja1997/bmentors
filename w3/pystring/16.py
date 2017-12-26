def stri16():
    a=input("enter a string : ")
    b=input("enter a string you want to enter between the first one : ")
    a=a[:(len(a)//2)]+b+a[(len(a)//2):]
    print(a)
    
    
