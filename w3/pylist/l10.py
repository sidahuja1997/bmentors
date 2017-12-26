def l10():
    a=input("Enter a string a bit long : ")
    a=a.split()
    n=int(input("Enter a number for alphabets : "))
    l=[]
    for i in a :
        if(len(i)>=n):
            l+=[i]
    print(l)
    
