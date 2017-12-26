def stri8():
    a=input("enter a string : ")
    a=a.split()
    maxx=0
    for i in a:
        if(len(i)>= maxx):
            maxx=len(i)
        else :
            pass

    
    print(maxx)
    return(maxx)
